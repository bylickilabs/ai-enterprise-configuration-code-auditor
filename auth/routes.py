# auth/routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from auth.service import create_user, delete_user, list_users, rotate_token, authenticate
from app.i18n import t

router = APIRouter(prefix="/auth", tags=["auth"])

def require_auth(token: str = Query(...), lang: str = Query("en")):
    user = authenticate(token)
    if not user:
        raise HTTPException(status_code=401, detail=t(lang, "unauthorized"))
    return user

@router.post("/users")
def api_create_user(
    username: str,
    role: str,
    user=Depends(require_auth),
    lang: str = "en"
):
    if user.role != "Admin":
        raise HTTPException(status_code=403, detail=t(lang, "forbidden"))
    return create_user(username, role)

@router.delete("/users/{username}")
def api_delete_user(
    username: str,
    user=Depends(require_auth),
    lang: str = "en"
):
    if user.role != "Admin":
        raise HTTPException(status_code=403, detail=t(lang, "forbidden"))
    delete_user(username)
    return {"status": "ok"}

@router.get("/users")
def api_list_users(user=Depends(require_auth)):
    return list_users()

@router.post("/rotate-token")
def api_rotate_token(
    username: str,
    user=Depends(require_auth),
    lang: str = "en"
):
    if user.role != "Admin":
        raise HTTPException(status_code=403, detail=t(lang, "forbidden"))
    return {"token": rotate_token(username)}
