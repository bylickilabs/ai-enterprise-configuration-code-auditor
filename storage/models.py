from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from storage.db import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    active = Column(Integer, default=1)

class AuditLogDB(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    user = Column(String)
    role = Column(String)
    action = Column(String)
    details = Column(Text)

class ScanDB(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    profile = Column(String, nullable=False)
    files_scanned = Column(Integer, nullable=False)
    risk_score = Column(Integer, nullable=False)
    risk_level = Column(String, nullable=False)
    lang = Column(String, nullable=False)

    findings = relationship(
        "FindingDB",
        back_populates="scan",
        cascade="all, delete-orphan"
    )

class FindingDB(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True)
    scan_id = Column(Integer, ForeignKey("scans.id"), nullable=False)

    severity = Column(String, nullable=False)   # LOW / MEDIUM / HIGH / CRITICAL
    file = Column(Text, nullable=False)
    message = Column(Text, nullable=False)

    scan = relationship("ScanDB", back_populates="findings")
