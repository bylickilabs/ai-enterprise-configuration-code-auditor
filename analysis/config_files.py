from pathlib import Path
from compliance.engine import evaluate

CONFIG_EXT = {".env", ".yml", ".yaml", ".json"}

def analyze_configs(base: Path, profile: str) -> list[dict]:
    results = []

    for file in base.rglob("*"):
        if file.suffix.lower() in CONFIG_EXT:
            try:
                content = file.read_text(errors="ignore").lower()
            except Exception:
                continue

            findings = evaluate(content, profile)
            for f in findings:
                results.append({
                    "category": "Config",
                    "file": str(file),
                    "rule": f["rule"],
                    "severity": f["severity"],
                    "message": f["message"]
                })

    return results
