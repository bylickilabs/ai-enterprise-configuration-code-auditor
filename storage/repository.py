import json
from typing import List, Optional

from sqlalchemy.orm import Session

from storage.db import SessionLocal
from storage.models import (
    UserDB,
    AuditLogDB,
    ScanDB,
    FindingDB,
)

def get_session() -> Session:
    return SessionLocal()

def create_user(username: str, role: str, token: str) -> UserDB:
    db = get_session()
    try:
        user = UserDB(username=username, role=role, token=token)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()


def get_user_by_token(token: str) -> Optional[UserDB]:
    db = get_session()
    try:
        return (
            db.query(UserDB)
            .filter(UserDB.token == token, UserDB.active == 1)
            .first()
        )
    finally:
        db.close()


def list_users() -> List[UserDB]:
    db = get_session()
    try:
        return db.query(UserDB).all()
    finally:
        db.close()

def log_audit(user: str, role: str, action: str, details=None) -> None:
    db = get_session()
    try:
        entry = AuditLogDB(
            user=user,
            role=role,
            action=action,
            details=json.dumps(details or {})
        )
        db.add(entry)
        db.commit()
    finally:
        db.close()

def save_scan(result: dict, lang: str) -> int:
    """
    Persist a scan result including all findings.
    Returns scan ID.
    """
    db = get_session()

    try:
        scan = ScanDB(
            profile=result["profile"],
            files_scanned=result["files_scanned"],
            risk_score=result["risk_score"],
            risk_level=result["risk_level_code"],
            lang=lang,
        )
        db.add(scan)
        db.flush()

        for f in result.get("findings", []):
            finding = FindingDB(
                scan_id=scan.id,
                severity=f["severity_code"],
                file=f["file"],
                message=f["message"],
            )
            db.add(finding)

        db.commit()
        return scan.id

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def list_scans(limit: int = 50) -> List[ScanDB]:
    """
    Return latest scans (without findings).
    """
    db = get_session()
    try:
        return (
            db.query(ScanDB)
            .order_by(ScanDB.timestamp.desc())
            .limit(limit)
            .all()
        )
    finally:
        db.close()


def get_scan(scan_id: int) -> Optional[ScanDB]:
    """
    Return a single scan including findings.
    """
    db = get_session()
    try:
        return (
            db.query(ScanDB)
            .filter(ScanDB.id == scan_id)
            .first()
        )
    finally:
        db.close()
