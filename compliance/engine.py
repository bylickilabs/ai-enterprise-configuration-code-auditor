from compliance.profiles import COMPLIANCE_PROFILES

def evaluate(content: str, profile: str) -> list[dict]:
    findings = []
    ruleset = COMPLIANCE_PROFILES.get(profile)

    if not ruleset:
        return findings

    for rule in ruleset["rules"]:
        if rule in content:
            findings.append({
                "rule": rule,
                "severity": ruleset["severity"],
                "message": f"Rule triggered: {rule}"
            })
    return findings
