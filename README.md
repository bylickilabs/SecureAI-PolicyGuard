# 🛡️ SecureAI PolicyGuard  
BYLICKILABS – Intelligence Systems & Communications  

![Version](https://img.shields.io/badge/version-1.1.0-blue.svg) | ![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg) | ![License: MIT](https://img.shields.io/badge/license-MIT-green.svg) | ![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-lightgrey.svg) | ![API Status](https://img.shields.io/badge/API-OAS%203.1-purple.svg) | ![Audit](https://img.shields.io/badge/Audit-Enabled-important.svg) | ![Security](https://img.shields.io/badge/Encryption-AES--256-critical.svg) |
|---|---|---|---|---|---|---|



# 🔐 SecureAI PolicyGuard  
**Enterprise Compliance & Encryption AI**  
BYLICKILABS – Intelligence Systems & Communications  

---

## 📌 Overview
SecureAI PolicyGuard is an AI-driven enterprise data protection platform combining **automated classification**, **policy-based encryption**, and **audit-grade compliance logging**.  
It bridges security operations, compliance, and IT automation with a dual-layer **Desktop + REST API architecture**.

---

## 🚀 Core Capabilities

| Capability | Description |
|-------------|-------------|
| **AI Classification Engine** | Detects sensitive content and calculates contextual risk scores |
| **Policy Mapping Engine** | Maps classification levels to automatic actions (Encrypt / Log / Ignore) |
| **Encryption Layer (AES-256)** | Local, per-directory key management using Fernet for authenticated encryption |
| **Audit Logging** | SQLite-based, immutable record of classification and encryption events |
| **REST API (FastAPI + OAS 3.1)** | Standardized interface for automation and remote analysis |
| **Multi-Language GUI (DE/EN)** | Dual-language interface for global operations |
| **Batch Automation Script** | One-click startup linking API server and GUI seamlessly |

---

## 🏗️ Architecture Overview

```
+---------------------------------------------------+
| SecureAI PolicyGuard – Desktop GUI                |
|  - Configuration UI                               |
|  - File scanning and visualization                |
+---------------------------------------------------+
                      |
                      v
+---------------------------------------------------+
| Classifier Engine                                 |
|  - Heuristic + ML entity detection                |
|  - Risk calculation                               |
+---------------------------------------------------+
                      |
                      v
+---------------------------------------------------+
| Policy Engine                                     |
|  - Confidentiality mapping                        |
|  - Action rules                                   |
+---------------------------------------------------+
                      |
                      v
+---------------------------------------------------+
| Crypto Engine (Fernet / AES-256)                  |
|  - Local encryption per workspace key             |
|  - Secure key rotation and storage                |
+---------------------------------------------------+
                      |
                      v
+---------------------------------------------------+
| Audit Database (SQLite)                           |
|  - Risk score, classification, entities, actions  |
+---------------------------------------------------+
                      |
                      +--> REST API (FastAPI / OAS 3.1)
```

---

## ⚙️ Installation Guide

### Prerequisites
- Windows 10/11 (64-bit)
- Python 3.10+ (Recommended: 3.12)
- Internet access for dependency installation

### Steps
```bash
pip install -r requirements.txt
```

---

## ▶️ Launch Methods

### Method A – Manual
```bash
python main.py
```

### Method B – Automated (API + GUI)
```bash
run_secureai.bat
```

**API Endpoints:**  
- http://127.0.0.1:8000/health  
- http://127.0.0.1:8000/docs  

---

## 🔌 REST API Example

### Request
```http
POST /analyze-text
Content-Type: application/json

{
  "text": "Customer IBAN: DE11 2222 3333 4444 00"
}
```

### Response
```json
{
  "classification": "Highly_Confidential",
  "risk_score": 88,
  "entities": [["iban", "DE44...31"]]
}
```

---

## 🧱 Default Policy Matrix

| Classification | Risk Range | Action |
|----------------|-------------|--------|
| PUBLIC | 0–29 | Ignore |
| INTERNAL | 30–59 | Log Only |
| CONFIDENTIAL | 60–79 | Encrypt |
| HIGHLY_CONFIDENTIAL | 80–100 | Encrypt + Flag |

---

## 🗄️ Audit Logging Schema

| Field | Description |
|-------|--------------|
| file_path | Path of analyzed file |
| classification | Detected sensitivity level |
| risk_score | Calculated risk score |
| entity_count | Number of detected entities |
| timestamp | Timestamp of operation |

Stored in local SQLite database per workspace.

---

## 🧩 Integration Targets
- Security Operation Centers (SOC)  
- Compliance & Audit Departments  
- Regulated industries (Finance, Energy, Government)  
- Data Protection & Forensics Teams  

---

## 🧪 API Certification & Testing
SecureAI PolicyGuard includes automated **Schemathesis-based API certification tests** verifying OpenAPI 3.1 contract integrity.  
All test results are stored under `/tests/logs/` for compliance evidence.

---

## 🧠 Credits
Developed by **Thorsten Bylicki**  
**BYLICKILABS – Intelligence Systems & Communications**  

---

## 📜 License
© 2025 BYLICKILABS. Proprietary License.  
Use only with explicit authorization.

---

