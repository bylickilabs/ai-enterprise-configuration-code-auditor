from pathlib import Path

IGNORE_FILE = ".auditignore"

def load_ignore_rules(base: Path) -> dict:
    rules = {"files": set(), "rules": set()}

    ignore_path = base / IGNORE_FILE
    if not ignore_path.exists():
        return rules

    for line in ignore_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("file:"):
            rules["files"].add(line.replace("file:", "").strip())
        if line.startswith("rule:"):
            rules["rules"].add(line.replace("rule:", "").strip())

    return rules

def is_ignored(finding: dict) -> bool:
    file = Path(finding.get("file", "")).name
    rule = finding.get("rule")

    # Lazy-load per finding (safe, small overhead)
    base = Path(finding.get("file", "")).parent
    rules = load_ignore_rules(base)

    return file in rules["files"] or rule in rules["rules"]
