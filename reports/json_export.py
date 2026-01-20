from app.config import APP_NAME, APP_VERSION, APP_COMPANY
from reports.signer import sign_report

def export_json(scan_result: dict, lang: str) -> dict:
    payload = {
        "application": APP_NAME,
        "version": APP_VERSION,
        "company": APP_COMPANY,
        "language": lang,
        "risk": {
            "score": scan_result["score"],
            "level": scan_result["risk_level"],
        },
        "findings": scan_result["findings"]
    }

    payload["signature"] = sign_report(payload)
    return payload
