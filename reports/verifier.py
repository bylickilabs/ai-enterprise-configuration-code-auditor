from reports.signer import sign_report

def verify_report(payload: dict, signature: str) -> bool:
    """
    Verifies SHA-256 signature.
    """
    return sign_report(payload) == signature
