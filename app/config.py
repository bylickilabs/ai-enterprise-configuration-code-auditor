from pathlib import Path
import os

APP_NAME = "ai-enterprise-configuration-code-auditor"

APP_TITLE = {
    "de": "AI Enterprise Konfigurations- & Code Auditor",
    "en": "AI Enterprise Configuration & Code Auditor",
}

APP_VERSION = "1.0.0"
APP_COMPANY = "BYLICKILABS"

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = DATA_DIR / "logs"

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "app.db"

DB_URL = os.getenv(
    "DB_URL",
    f"sqlite:///{DB_PATH}"
)

SUPPORTED_LANGUAGES = ["de", "en"]
DEFAULT_LANGUAGE = "en"

ROLES = ["Admin", "Auditor", "Viewer"]

BOOTSTRAP_ADMIN_TOKEN = os.getenv(
    "BOOTSTRAP_ADMIN_TOKEN",
    "admin-dev-token"
)

BOOTSTRAP_ADMIN_USER = {
    "username": "admin",
    "role": "Admin",
}

RISK_THRESHOLDS = {
    "LOW": 20,
    "MEDIUM": 50,
    "HIGH": 80,
}

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
