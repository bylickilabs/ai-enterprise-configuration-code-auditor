from pathlib import Path
from compliance.engine import evaluate

def analyze_docker(base: Path, profile: str) -> list[dict]:
    results = []

    for file in base.rglob("*"):
        if file.name.lower() == "dockerfile":
            try:
                content = file.read_text(errors="ignore").lower()
            except Exception:
                continue

            findings = evaluate(content, profile)
            for f in findings:
                results.append({
                    "category": "Docker",
                    "file": str(file),
                    "rule": f["rule"],
                    "severity": f["severity"],
                    "message": f["message"]
                })

    return results
