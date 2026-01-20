import tempfile

from fastapi import (
    FastAPI,
    Request,
    UploadFile,
    File,
    Form,
)
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

from app.config import (
    APP_NAME,
    APP_VERSION,
    DEFAULT_LANGUAGE,
)

from analysis.scanner import scan_project
from storage.db import init_db
from storage.repository import save_scan, list_scans, get_scan
from app.i18n import t

init_db()

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)
app.mount("/static", StaticFiles(directory="ui/static"), name="static")
templates = Jinja2Templates(directory="ui/templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request, lang: str = DEFAULT_LANGUAGE):
    scans = list_scans(limit=10)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "lang": lang,
            "app_name": APP_NAME,
            "app_version": APP_VERSION,
            "scans": scans,
        },
    )

@app.post("/scan", response_class=HTMLResponse)
async def scan(
    request: Request,
    file: UploadFile = File(...),
    profile: str = Form("BASE"),
    token: str = Form(...),
    lang: str = Form(DEFAULT_LANGUAGE),
):

    if token != "admin-dev-token":
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "lang": lang,
                "app_name": APP_NAME,
                "app_version": APP_VERSION,
                "error": t(lang, "auth.invalid_token"),
            },
        )

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        zip_path = tmp.name

    try:
        result = scan_project(zip_path, profile, lang)
        scan_id = save_scan(result, lang)
        result["scan_id"] = scan_id
    except Exception as exc:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "lang": lang,
                "app_name": APP_NAME,
                "app_version": APP_VERSION,
                "error": str(exc),
            },
        )

    scans = list_scans(limit=10)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "lang": lang,
            "app_name": APP_NAME,
            "app_version": APP_VERSION,
            "result": result,
            "scans": scans,
        },
    )

@app.get("/scan/{scan_id}", response_class=HTMLResponse)
def scan_detail(request: Request, scan_id: int, lang: str = DEFAULT_LANGUAGE):
    scan = get_scan(scan_id)

    if not scan:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "lang": lang,
                "app_name": APP_NAME,
                "app_version": APP_VERSION,
                "error": t(lang, "error.not_found"),
            },
        )

    scans = list_scans(limit=10)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "lang": lang,
            "app_name": APP_NAME,
            "app_version": APP_VERSION,
            "scan_detail": scan,
            "scans": scans,
        },
    )

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "app": APP_NAME,
        "version": APP_VERSION,
    }

def main():
    print("🚀 UI + Scan aktiv – http://127.0.0.1:8000")
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )

if __name__ == "__main__":
    main()