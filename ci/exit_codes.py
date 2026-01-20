EXIT_CODES = {
    "LOW": 0,
    "MEDIUM": 0,
    "HIGH": 1,
    "CRITICAL": 2,
}

def exit_code_for_risk(risk_level: str) -> int:
    return EXIT_CODES.get(risk_level.upper(), 2)
