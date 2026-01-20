import json
from datetime import datetime
from app.config import LOG_DIR

AUDIT_LOG_FILE = LOG_DIR / "audit_log.jsonl"

def log_event(
    user: str,
    role: str,
    action: str,
    details: dict | None = None
):
    """
    Writes an immutable audit event.
    """
    event = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user": user,
        "role": role,
        "action": action,
        "details": details or {}
    }

    with open(AUDIT_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")