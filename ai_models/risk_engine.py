from typing import List, Tuple

Entity = Tuple[str, str]


def compute_risk_score(text: str, entities: List[Entity]) -> int:
    """
    Heuristische Risk-Engine, liefert einen Risiko-Score von 0–100.
    Kann später durch ein echtes ML/NLP-Modell ersetzt werden.
    """
    score = 0
    lower = text.lower()

    length = len(text)
    if length > 2000:
        score += 10
    elif length > 500:
        score += 5

    high_risk_keywords = [
        "password", "passwort", "iban", "konto", "kontonummer",
        "gehalt", "salary", "api key", "secret", "token", "vertrag",
        "personal", "hr", "payroll",
    ]

    medium_risk_keywords = [
        "internal", "intern", "sensitive", "vertraulich", "confidential",
        "customer", "kunde", "client", "report",
    ]

    for kw in high_risk_keywords:
        if kw in lower:
            score += 15

    for kw in medium_risk_keywords:
        if kw in lower:
            score += 5

    weights = {
        "IBAN": 25,
        "CREDIT_CARD": 25,
        "API_KEY": 25,
        "PASSWORD": 25,
        "EMAIL": 10,
        "PERSON": 8,
        "ORG": 5,
        "LOCATION": 3,
    }

    for label, _ in entities:
        score += weights.get(label, 1)

    return max(0, min(100, score))
