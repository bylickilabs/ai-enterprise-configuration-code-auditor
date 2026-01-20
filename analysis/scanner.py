import zipfile
from pathlib import Path
from typing import Dict, List

from app.i18n import t, risk_label, profile_label

SENSITIVE_EXTENSIONS = {
    ".env": "HIGH",
    ".key": "CRITICAL",
    ".pem": "CRITICAL",
    ".pfx": "CRITICAL",
    ".crt": "MEDIUM",
}

SENSITIVE_FILENAMES = {
    ".env": "HIGH",
    "config.env": "HIGH",
    "id_rsa": "CRITICAL",
}


RISK_POINTS = {
    "LOW": 5,
    "MEDIUM": 15,
    "HIGH": 30,
    "CRITICAL": 50,
}

def scan_project(zip_path: str, profile: str, lang: str = "en") -> Dict:
    """
    Scan a ZIP archive and return structured, localized results.
    """

    if not zipfile.is_zipfile(zip_path):
        raise ValueError(t(lang, "scan.invalid_zip"))

    findings: List[Dict] = []
    files_scanned = 0
    total_risk_score = 0

    profile_name = profile_label(lang, profile)

    with zipfile.ZipFile(zip_path, "r") as zf:
        for member in zf.infolist():
            if member.is_dir():
                continue

            files_scanned += 1
            path = Path(member.filename)
            name = path.name.lower()
            ext = path.suffix.lower()

            severity = None

            if name in SENSITIVE_FILENAMES:
                severity = SENSITIVE_FILENAMES[name]

            elif ext in SENSITIVE_EXTENSIONS:
                severity = SENSITIVE_EXTENSIONS[ext]

            if not severity:
                continue

            total_risk_score += RISK_POINTS[severity]

            findings.append({
                "severity": risk_label(lang, severity),
                "file": member.filename,
                "message": _finding_message(lang, severity),
                "severity_code": severity,
            })

    risk_level = _calculate_risk_level(total_risk_score)

    return {
        "profile": profile_name,
        "files_scanned": files_scanned,
        "risk_score": total_risk_score,
        "risk_level": risk_label(lang, risk_level),
        "risk_level_code": risk_level,
        "findings": findings,
    }

def _calculate_risk_level(score: int) -> str:
    if score >= 80:
        return "CRITICAL"
    if score >= 50:
        return "HIGH"
    if score >= 20:
        return "MEDIUM"
    return "LOW"


def _finding_message(lang: str, severity: str) -> str:
    """
    Centralized finding messages (translated).
    """
    if severity == "CRITICAL":
        return t(
            lang,
            "risk.desc.critical"
        )
    if severity == "HIGH":
        return t(
            lang,
            "risk.desc.high"
        )
    if severity == "MEDIUM":
        return t(
            lang,
            "risk.desc.medium"
        )
    return t(
        lang,
        "risk.desc.low"
    )
