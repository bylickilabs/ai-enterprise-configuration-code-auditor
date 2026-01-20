from fastapi import APIRouter, Depends, HTTPException
from tenants.service import create_tenant, list_tenants
from auth.routes import require_auth
from app.i18n import t

router = APIRouter(prefix="/tenants", tags=["tenants"])

@router.post("/")
def api_create_tenant(
    name: str,
    license_type: str,
    user=Depends(require_auth),
    lang: str = "en"
):
    if user.role != "Admin":
        raise HTTPException(403, t(lang, "forbidden"))

    return create_tenant(name, license_type, user.username, user.role)

@router.get("/")
def api_list_tenants(user=Depends(require_auth)):
    return list_tenants()
