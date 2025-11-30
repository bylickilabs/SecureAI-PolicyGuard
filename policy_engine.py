def get_policy_for_decision(classification: str, risk_score: int, entities: list) -> dict:
    """
    Leitet aus Klassifikation, Risk-Score und Entitäten die Policy ab.
    """
    policy = {
        "encrypt": False,
        "target_dir": None,
        "log_only": False,
    }

    if classification == "PUBLIC":
        policy["log_only"] = True
    elif classification == "INTERNAL":
        policy["log_only"] = True
    elif classification == "CONFIDENTIAL":
        policy["encrypt"] = True
        policy["target_dir"] = "SecureArchive/CONFIDENTIAL"
    elif classification == "HIGHLY_CONFIDENTIAL":
        policy["encrypt"] = True
        policy["target_dir"] = "SecureArchive/HIGHLY_CONFIDENTIAL"

    if risk_score >= 85:
        policy["encrypt"] = True
        if policy["target_dir"] is None:
            policy["target_dir"] = "SecureArchive/HIGH_RISK"

    return policy
