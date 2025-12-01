from app_meta import APP_NAME, APP_VERSION, APP_COMPANY

LANG = {
    "de": {
        "window_title": f"{APP_NAME} – KI-gestützte Verschlüsselungs-Policies",
        "lang_de": "DE",
        "lang_en": "EN",

        "label_directory": "Basisverzeichnis:",
        "button_browse": "Durchsuchen …",
        "button_scan": "Scannen & Richtlinien anwenden",
        "button_info": "Info",
        "button_github": "GitHub",

        "label_api_mode": "API-Modus aktivieren:",
        "label_api_url": "API-Basis-URL:",

        "column_file": "Datei",
        "column_classification": "Klassifizierung",
        "column_risk": "Risiko",
        "column_action": "Aktion",

        "status_ready": "Bereit.",
        "status_scanning": "AI-Analyse läuft … bitte warten.",
        "status_done": "Scan abgeschlossen.",
        "status_error": "Fehler beim Scan – Details in der Konsole.",
        "status_api_error": "API-Fehler – Fallback auf lokale Analyse.",

        "msg_no_dir_title": "Kein Verzeichnis",
        "msg_no_dir_body": "Bitte wählen Sie zuerst ein Basisverzeichnis aus.",

        "msg_scan_finished_title": "Scan abgeschlossen",
        "msg_scan_finished_body": "Der Scan wurde abgeschlossen.\nAnzahl analysierter Dateien: {count}",

        "classification_PUBLIC": "Öffentlich",
        "classification_INTERNAL": "Intern",
        "classification_CONFIDENTIAL": "Vertraulich",
        "classification_HIGHLY_CONFIDENTIAL": "Streng vertraulich",

        "action_ENCRYPTED": "Verschlüsselt",
        "action_LOG_ONLY": "Nur protokolliert",
        "action_NONE": "Keine Maßnahme",
        "action_ERROR": "Fehler",

        "info_title": "Informationen zur Anwendung",
        "info_body": (
            f"{APP_NAME}\n"
            f"Version: {APP_VERSION}\n"
            f"Unternehmen: {APP_COMPANY}\n\n"
            "SecureAI PolicyGuard ist eine KI-unterstützte Sicherheitsanwendung zur "
            "automatisierten Klassifizierung sensibler Daten und zum Richtlinien-basierten "
            "Verschlüsselungs-Workflow. Die Anwendung analysiert Dateien, bewertet das Risiko "
            "und führt – abhängig von den Policies – automatisiert Verschlüsselung und Logging durch.\n\n"
            "Ab Version 1.1.0 steht zusätzlich eine optionale HTTP-API zur Verfügung, "
            "über die externe Systeme Analysen anfragen können."
        ),

        "detail_title": "AI-Analyse & Entscheidungsgrundlage",
        "detail_file": "Datei",
        "detail_classification": "Klassifizierung",
        "detail_risk": "Risiko-Score",
        "detail_explanation": "Begründung",

        "ai_core_idle": "AI Core: Bereit",
        "ai_core_active_label": "SECUREAI CORE – AKTIV",
        "ai_core_idle_label": "SECUREAI CORE",

        "ai_spinner_frames": [
            "Ich analysiere das Datensignal …",
            "Ich erkenne sensible Entitäten …",
            "Ich bewerte das Risikoprofil …",
            "Ich berechne passende Sicherheitsrichtlinien …",
            "Ich löse die finale Entscheidung aus …",
        ],

        "ai_explain_header": "Ich habe diese Datei ausgewertet und eine Einstufung vorgenommen.",
        "ai_explain_risk": "Mein aktueller Risiko-Score für diese Datei liegt bei {score}/100.",
        "ai_explain_no_entities": (
            "Ich konnte keine klaren sensiblen Entitäten erkennen. "
            "Ich nutze daher vor allem Struktur, Inhaltstyp und Kontext als Entscheidungsgrundlage."
        ),
        "ai_explain_entities_prefix": "Ich habe folgende sensible Entitäten erkannt:",
        "ai_explain_entities_item": "- {label}: {count} Vorkommen",
        "ai_explain_recommend_encrypt": (
            "Auf Basis dieser Bewertung empfehle ich dir eindeutig, "
            "diese Datei zu verschlüsseln und nur kontrolliert bereitzustellen."
        ),
        "ai_explain_recommend_monitor": (
            "Aktuell genügt eine Protokollierung und Überwachung. "
            "Eine erzwungene Verschlüsselung ist aus meiner Sicht nicht zwingend, "
            "kann aber je nach Policy sinnvoll sein."
        ),

        "entity_EMAIL": "E-Mail-Adresse",
        "entity_IBAN": "IBAN",
        "entity_CREDIT_CARD": "Kreditkartennummer",
        "entity_API_KEY": "API-Schlüssel/Token",
        "entity_PASSWORD": "Passwortfeld",
        "entity_PERSON": "Personenname",
        "entity_ORG": "Organisation",
        "entity_LOCATION": "Ort",

        "ai_hint_confidential": (
            "Ich sehe personenbezogene oder geschäftskritische Informationen. "
            "Ich empfehle dringend eine starke Verschlüsselung."
        ),
        "ai_hint_public": (
            "Die Inhalte wirken unkritisch. Aus meiner Sicht kann diese Datei als öffentlich behandelt werden, "
            "sofern keine weitergehenden Compliance-Vorgaben bestehen."
        ),
    },

    "en": {
        "window_title": f"{APP_NAME} – AI-powered Encryption Policies",
        "lang_de": "DE",
        "lang_en": "EN",

        "label_directory": "Base directory:",
        "button_browse": "Browse…",
        "button_scan": "Scan & apply policies",
        "button_info": "Info",
        "button_github": "GitHub",

        "label_api_mode": "Enable API mode:",
        "label_api_url": "API base URL:",

        "column_file": "File",
        "column_classification": "Classification",
        "column_risk": "Risk",
        "column_action": "Action",

        "status_ready": "Ready.",
        "status_scanning": "AI analysis in progress…",
        "status_done": "Scan completed.",
        "status_error": "Error during scan – see console for details.",
        "status_api_error": "API error – falling back to local analysis.",

        "msg_no_dir_title": "No directory selected",
        "msg_no_dir_body": "Please select a base directory first.",

        "msg_scan_finished_title": "Scan completed",
        "msg_scan_finished_body": "Scan finished.\nNumber of analyzed files: {count}",

        "classification_PUBLIC": "Public",
        "classification_INTERNAL": "Internal",
        "classification_CONFIDENTIAL": "Confidential",
        "classification_HIGHLY_CONFIDENTIAL": "Highly confidential",

        "action_ENCRYPTED": "Encrypted",
        "action_LOG_ONLY": "Logged only",
        "action_NONE": "No action",
        "action_ERROR": "Error",

        "info_title": "Application information",
        "info_body": (
            f"{APP_NAME}\n"
            f"Version: {APP_VERSION}\n"
            f"Company: {APP_COMPANY}\n\n"
            "SecureAI PolicyGuard is an AI-assisted security application for automatic "
            "classification of sensitive data and policy-driven encryption workflows. "
            "The application analyzes files, evaluates risk and, based on defined policies, "
            "automatically executes encryption and logging.\n\n"
            "Starting with version 1.1.0 an optional HTTP API is available so external systems "
            "can request analyses online."
        ),

        "detail_title": "AI analysis & decision basis",
        "detail_file": "File",
        "detail_classification": "Classification",
        "detail_risk": "Risk score",
        "detail_explanation": "Explanation",

        "ai_core_idle": "AI Core: Idle",
        "ai_core_active_label": "SECUREAI CORE – ACTIVE",
        "ai_core_idle_label": "SECUREAI CORE",

        "ai_spinner_frames": [
            "I'm analyzing the data signal …",
            "I'm detecting sensitive entities …",
            "I'm evaluating the risk profile …",
            "I'm computing the appropriate security policies …",
            "I'm triggering the final decision …",
        ],

        "ai_explain_header": "I've analyzed this file and determined a classification.",
        "ai_explain_risk": "My current risk score for this file is {score}/100.",
        "ai_explain_no_entities": (
            "I couldn't clearly detect sensitive entities. "
            "I'm basing my decision mainly on structure, content type and context."
        ),
        "ai_explain_entities_prefix": "I've detected the following sensitive entities:",
        "ai_explain_entities_item": "- {label}: {count} occurrences",
        "ai_explain_recommend_encrypt": (
            "Based on this evaluation, I strongly recommend encrypting this file "
            "and limiting access to controlled environments."
        ),
        "ai_explain_recommend_monitor": (
            "For now, logging and monitoring are sufficient. "
            "Forced encryption is not strictly required from my perspective, "
            "but may still be useful depending on your policies."
        ),

        "entity_EMAIL": "Email address",
        "entity_IBAN": "IBAN",
        "entity_CREDIT_CARD": "Credit card number",
        "entity_API_KEY": "API key/token",
        "entity_PASSWORD": "Password field",
        "entity_PERSON": "Person name",
        "entity_ORG": "Organization",
        "entity_LOCATION": "Location",

        "ai_hint_confidential": (
            "I see personal or business-critical information. "
            "I strongly recommend strong encryption."
        ),
        "ai_hint_public": (
            "The contents appear non-critical. From my perspective, this file can be treated as public, "
            "as long as no stricter compliance rules apply."
        ),
    },
}
