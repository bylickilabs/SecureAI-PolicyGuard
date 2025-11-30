import requests


def analyze_text_remote(text: str, base_url: str) -> dict:
    """
    Ruft die /analyze-text API auf und liefert das Ergebnis als dict.
    """
    url = base_url.rstrip("/") + "/analyze-text"
    resp = requests.post(url, json={"text": text}, timeout=10)
    resp.raise_for_status()
    return resp.json()
