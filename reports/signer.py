import hashlib
import json

def sign_report(payload: dict) -> str:
    """
    Generates SHA-256 signature over canonical JSON payload.
    """
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
