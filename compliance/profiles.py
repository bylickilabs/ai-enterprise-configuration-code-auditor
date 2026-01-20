from app.i18n import t

COMPLIANCE_PROFILES = {
    "BASE": {
        "rules": ["eval(", "exec("],
        "severity": "HIGH"
    },
    "OWASP": {
        "rules": ["eval(", "exec(", "password", "token", "apikey"],
        "severity": "HIGH"
    },
    "CIS": {
        "rules": ["latest", "user root"],
        "severity": "MEDIUM"
    }
}

def list_profiles(lang: str):
    return {
        "BASE": t(lang, "profile_base"),
        "OWASP": t(lang, "profile_owasp"),
        "CIS": t(lang, "profile_cis")
    }
