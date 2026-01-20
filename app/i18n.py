from typing import Dict

I18N: Dict[str, Dict[str, str]] = {

    "de": {

        "app.name": "AI Enterprise Konfigurations- & Code Auditor",
        "app.company": "BYLICKILABS",
        "app.description":
            "Lokales Tool zur Sicherheits-, Konfigurations- und Compliance-Analyse von Softwareprojekten.",

        "auth.unauthorized": "Nicht autorisiert",
        "auth.forbidden": "Zugriff verweigert",
        "auth.invalid_token": "Ungültiger API-Token",
        "auth.login_success": "Anmeldung erfolgreich",
        "auth.login_failed": "Anmeldung fehlgeschlagen",

        "scan.started": "Scan gestartet",
        "scan.completed": "Scan abgeschlossen",
        "scan.failed": "Scan fehlgeschlagen",
        "scan.invalid_zip": "Die hochgeladene Datei ist kein gültiges ZIP-Archiv",
        "scan.no_files": "Keine auswertbaren Dateien gefunden",

        "risk.level.low": "Niedrig",
        "risk.level.medium": "Mittel",
        "risk.level.high": "Hoch",
        "risk.level.critical": "Kritisch",

        "risk.desc.low": "Geringes Risiko – keine unmittelbare Handlung erforderlich",
        "risk.desc.medium": "Mittleres Risiko – Überprüfung empfohlen",
        "risk.desc.high": "Hohes Risiko – zeitnahe Maßnahmen erforderlich",
        "risk.desc.critical": "Kritisches Risiko – sofortiger Handlungsbedarf",

        "profile.base": "Basisprofil",
        "profile.owasp": "OWASP-orientiertes Profil",
        "profile.cis": "CIS-orientiertes Profil",

        "audit.scan": "Projekt-Scan ausgeführt",
        "audit.login": "Benutzeranmeldung",
        "audit.user_create": "Benutzer erstellt",
        "audit.user_delete": "Benutzer gelöscht",
        "audit.config_change": "Konfiguration geändert",

        "report.title": "Sicherheitsanalyse-Bericht",
        "report.generated": "Bericht erstellt",
        "report.signed": "Bericht kryptografisch signiert",
        "report.export_json": "Bericht als JSON exportiert",
        "report.export_pdf": "Bericht als PDF exportiert",

        "error.internal": "Interner Serverfehler",
        "error.invalid_request": "Ungültige Anfrage",
        "error.not_found": "Ressource nicht gefunden",
    },

    "en": {

        "app.name": "AI Enterprise Configuration & Code Auditor",
        "app.company": "BYLICKILABS",
        "app.description":
            "Local tool for security, configuration and compliance analysis of software projects.",

        "auth.unauthorized": "Unauthorized",
        "auth.forbidden": "Access denied",
        "auth.invalid_token": "Invalid API token",
        "auth.login_success": "Login successful",
        "auth.login_failed": "Login failed",

        "scan.started": "Scan started",
        "scan.completed": "Scan completed",
        "scan.failed": "Scan failed",
        "scan.invalid_zip": "Uploaded file is not a valid ZIP archive",
        "scan.no_files": "No analyzable files found",

        "risk.level.low": "Low",
        "risk.level.medium": "Medium",
        "risk.level.high": "High",
        "risk.level.critical": "Critical",

        "risk.desc.low": "Low risk – no immediate action required",
        "risk.desc.medium": "Medium risk – review recommended",
        "risk.desc.high": "High risk – timely action required",
        "risk.desc.critical": "Critical risk – immediate action required",

        "profile.base": "Base profile",
        "profile.owasp": "OWASP-aligned profile",
        "profile.cis": "CIS-aligned profile",

        "audit.scan": "Project scan executed",
        "audit.login": "User login",
        "audit.user_create": "User created",
        "audit.user_delete": "User deleted",
        "audit.config_change": "Configuration changed",

        "report.title": "Security Analysis Report",
        "report.generated": "Report generated",
        "report.signed": "Report cryptographically signed",
        "report.export_json": "Report exported as JSON",
        "report.export_pdf": "Report exported as PDF",

        "error.internal": "Internal server error",
        "error.invalid_request": "Invalid request",
        "error.not_found": "Resource not found",
    }
}

def t(lang: str, key: str) -> str:
    """
    Translation helper.

    Fallback order:
    1. Requested language
    2. English
    3. Key itself (visible error)
    """
    if not lang:
        lang = "en"

    return (
        I18N.get(lang, {}).get(
            key,
            I18N.get("en", {}).get(key, key)
        )
    )

def risk_label(lang: str, level: str) -> str:
    """Translate risk level enum to localized label."""
    return t(lang, f"risk.level.{level.lower()}")

def risk_description(lang: str, level: str) -> str:
    """Translate risk level enum to localized description."""
    return t(lang, f"risk.desc.{level.lower()}")

def profile_label(lang: str, profile: str) -> str:
    """Translate compliance profile."""
    return t(lang, f"profile.{profile.lower()}")