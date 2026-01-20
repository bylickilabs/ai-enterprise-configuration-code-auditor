from pathlib import Path
from compliance.engine import evaluate

SUPPORTED_CODE_EXT = {".py", ".js", ".ts", ".sh"}

def analyze_code(base: Path, profile: str) -> list[dict]:
    results = []

    for file in base.rglob("*"):
        if file.suffix.lower() in SUPPORTED_CODE_EXT:
            try:
                content = file.read_text(errors="ignore").lower()
            except Exception:
                continue

            findings = evaluate(content, profile)
            for f in findings:
                results.append({
                    "category": "Code",
                    "file": str(file),
                    "rule": f["rule"],
                    "severity": f["severity"],
                    "message": f["message"]
                })

    return results
