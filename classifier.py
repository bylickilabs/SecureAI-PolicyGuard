from ai_models.risk_engine import compute_risk_score
from ai_models.ner_engine import extract_entities


def analyze_content(text: str) -> dict:
    """
    Führt Entity-Erkennung, Risiko-Skoring und Klassifikation durch.
    """
    entities = extract_entities(text)
    risk_score = compute_risk_score(text, entities)
    classification = classify_from_risk_and_entities(risk_score, entities)
    explanation = build_explanation(classification, risk_score, entities)
    return {
        "classification": classification,
        "risk_score": risk_score,
        "entities": entities,
        "explanation": explanation,
    }


def classify_from_risk_and_entities(risk_score: int, entities: list) -> str:
    if risk_score >= 80:
        return "HIGHLY_CONFIDENTIAL"
    if risk_score >= 60:
        return "CONFIDENTIAL"
    if risk_score >= 30:
        return "INTERNAL"
    return "PUBLIC"


def build_explanation(classification: str, risk_score: int, entities: list) -> str:
    summary = {}
    for label, _ in entities:
        summary[label] = summary.get(label, 0) + 1

    parts = [
        f"Klassifizierung / Classification: {classification}",
        f"Risiko-Score / Risk score: {risk_score}/100",
    ]

    if summary:
        ent_str = ", ".join(f"{k}: {v}" for k, v in summary.items())
        parts.append(f"Erkannte Entitäten / Detected entities: {ent_str}")
    else:
        parts.append("Keine klaren sensiblen Entitäten erkannt / No clear sensitive entities detected.")

    if classification in ("CONFIDENTIAL", "HIGHLY_CONFIDENTIAL"):
        parts.append("Empfehlung: Verschlüsselung und geschützte Ablage empfohlen.")
    else:
        parts.append("Empfehlung: Überwachung ausreichend, keine erzwungene Verschlüsselung.")

    return "\n".join(parts)
