from app.config import RISK_THRESHOLDS

SEVERITY_WEIGHTS = {
    "LOW": 5,
    "MEDIUM": 15,
    "HIGH": 30,
    "CRITICAL": 50
}

def calculate_score(findings: list[dict]) -> int:
    """
    Calculates total risk score based on findings.
    """
    score = 0
    for f in findings:
        score += SEVERITY_WEIGHTS.get(f["severity"], 0)
    return min(score, 100)

def classify_risk(score: int) -> str:
    """
    Maps numeric score to enterprise risk level.
    """
    if score < RISK_THRESHOLDS["LOW"]:
        return "LOW"
    if score < RISK_THRESHOLDS["MEDIUM"]:
        return "MEDIUM"
    if score < RISK_THRESHOLDS["HIGH"]:
        return "HIGH"
    return "CRITICAL"
