# auth/service.py
from typing import Optional

from app.config import (
    BOOTSTRAP_ADMIN_TOKEN,
    BOOTSTRAP_ADMIN_USER,
)

from storage.database import SessionLocal
from storage.models import UserDB

def authenticate(token: str) -> Optional[dict]:
    """
    Authenticate user by API token.

    Order:
    1. Bootstrap admin token
    2. Database-backed users
    """

    if not token:
        return None

    if token == BOOTSTRAP_ADMIN_TOKEN:
        return {
            "username": BOOTSTRAP_ADMIN_USER["username"],
            "role": BOOTSTRAP_ADMIN_USER["role"],
            "source": "bootstrap",
        }

    db = SessionLocal()
    try:
        user = (
            db.query(UserDB)
            .filter(UserDB.token == token)
            .filter(UserDB.active == 1)
            .first()
        )

        if not user:
            return None

        return {
            "username": user.username,
            "role": user.role,
            "source": "database",
        }

    finally:
        db.close()

def create_user(username: str, role: str, token: str) -> None:
    db = SessionLocal()
    try:
        user = UserDB(
            username=username,
            role=role,
            token=token,
            active=1,
        )
        db.add(user)
        db.commit()
    finally:
        db.close()
