import re
from typing import List, Tuple

Entity = Tuple[str, str]


def extract_entities(text: str) -> List[Entity]:
    """
    Einfache, regex-basierte Erkennung sensibler Entitäten.
    """
    entities: List[Entity] = []

    for m in re.finditer(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text):
        entities.append(("EMAIL", m.group(0)))

    for m in re.finditer(r'\b[A-Z]{2}\d{2}[A-Z0-9]{10,30}\b', text):
        entities.append(("IBAN", m.group(0)))

    for m in re.finditer(r'\b\d{16}\b', text):
        entities.append(("CREDIT_CARD", m.group(0)))

    if re.search(r'(api_key|api key|secret_key|token=)', text, re.IGNORECASE):
        entities.append(("API_KEY", "generic_api_secret"))

    if re.search(r'password\s*[:=]', text, re.IGNORECASE):
        entities.append(("PASSWORD", "password_field"))

    for m in re.finditer(r'\b[A-ZÄÖÜ][a-zäöüß]+ [A-ZÄÖÜ][a-zäöüß]+\b', text):
        entities.append(("PERSON", m.group(0)))

    for m in re.finditer(r'\b(GmbH|AG|Inc\.|Corp\.|Ltd\.)\b', text):
        entities.append(("ORG", m.group(0)))

    return entities
