from licensing.models import LICENSE_TIERS
from storage.database import SessionLocal
from tenants.models import TenantDB
from fastapi import HTTPException

def enforce_feature(tenant_id: int, feature: str):
    db = SessionLocal()
    tenant = db.query(TenantDB).filter(TenantDB.id == tenant_id).first()
    db.close()

    if not tenant:
        raise HTTPException(404, "Tenant not found")

    allowed = LICENSE_TIERS.get(tenant.license_type, [])
    if feature not in allowed:
        raise HTTPException(
            status_code=403,
            detail=f"Feature '{feature}' not allowed for license '{tenant.license_type}'"
        )
