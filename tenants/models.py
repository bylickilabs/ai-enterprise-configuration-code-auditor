from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from storage.database import Base

class TenantDB(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    license_type = Column(String, nullable=False)
    active = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
