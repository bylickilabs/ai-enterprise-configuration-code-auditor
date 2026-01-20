from storage.database import SessionLocal
from tenants.models import TenantDB
from audit.logger import log_event

def create_tenant(name: str, license_type: str, actor: str, role: str):
    db = SessionLocal()
    tenant = TenantDB(name=name, license_type=license_type)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    db.close()

    log_event(actor, role, "tenant_create", {"tenant": name, "license": license_type})
    return tenant

def list_tenants():
    db = SessionLocal()
    tenants = db.query(TenantDB).filter(TenantDB.active == 1).all()
    db.close()
    return tenants

def get_tenant(tenant_id: int):
    db = SessionLocal()
    tenant = db.query(TenantDB).filter(TenantDB.id == tenant_id).first()
    db.close()
    return tenant
