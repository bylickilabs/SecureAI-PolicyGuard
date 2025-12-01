| [![🧠 SecureAI PolicyGuard – CI/CD Pipeline](https://github.com/bylickilabs/SecureAI-PolicyGuard/actions/workflows/main.yml/badge.svg)](https://github.com/bylickilabs/SecureAI-PolicyGuard/actions/workflows/main.yml) |
|---|

<div align="center">
  
# 🛡️ SecureAI PolicyGuard  
BYLICKILABS – Intelligence Systems & Communications  

![Version](https://img.shields.io/badge/version-1.1.0-blue.svg) | ![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg) | ![License: MIT](https://img.shields.io/badge/license-MIT-green.svg) | ![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-lightgrey.svg) | ![API Status](https://img.shields.io/badge/API-OAS%203.1-purple.svg) | ![Audit](https://img.shields.io/badge/Audit-Enabled-important.svg) | ![Security](https://img.shields.io/badge/Encryption-AES--256-critical.svg) |
|---|---|---|---|---|---|---|

</div>

---

## 📌 Overview
> SecureAI PolicyGuard is an AI-driven enterprise data protection platform combining 
- **automated classification**,
- **policy-based encryption**,
- **audit-grade compliance logging**.  
  - It bridges security operations, compliance, and IT automation with a dual-layer **Desktop + REST API architecture**.

<div align="center">

![line](https://github.com/bylickilabs/bylickilabs/assets/109308073/bfd77a60-d426-4470-b417-fdbab0166188) 

</div>

<div align="center">

<details>
  <summary>🎓 Certifications & Expertise</summary>

| ![certificate_of_completion_backend_developer_with_python (1)](https://github.com/user-attachments/assets/887a209c-e899-49bb-822b-51883354fd6d) |
|---|

| ![certificate_of_completion_fullstack_developer_with_python (1)](https://github.com/user-attachments/assets/390c7574-0e01-48f3-94e3-a5f74ced5ead) |
|---|

| ![certificate_of_completion_front_end_development](https://github.com/user-attachments/assets/57f19f4e-99be-46fc-8efd-37cecf3c21b0)  |
|---|

| ![certificate_of_completion_modern_web_development](https://github.com/user-attachments/assets/2fbfc420-d6d4-43cf-95e1-9756dc09cab9) |
|---|

| ![certificate_of_completion_html](https://github.com/user-attachments/assets/98a85fe5-7929-4baa-951a-664820af9e2d) |
|---|

| ![certificate_of_completion_css](https://github.com/user-attachments/assets/143eae2e-3493-41c1-97f8-7b5518cb0be9) |
|---|

| ![certificate_of_completion_javascript](https://github.com/user-attachments/assets/bff6b442-e34c-4dea-8d26-9f51bf696d93) |
|---|

| ![certificate_of_completion_bootstrap_5](https://github.com/user-attachments/assets/92102be2-ea0d-4eae-9698-04a05874429c) |
|---|

| ![certificate_of_completion_python](https://github.com/user-attachments/assets/e0741261-d519-4173-8ffe-dac8bbe821b3) |
|---|

| ![certificate_of_completion_numpy](https://github.com/user-attachments/assets/bb964f82-5a85-45ba-b84c-80d37ba95e7d) |
|---|

| ![certificate_of_completion_scipy](https://github.com/user-attachments/assets/34bada46-285a-4eb7-8559-e1b49f5965bc) |
|---|

| ![certificate_of_completion_data_science](https://github.com/user-attachments/assets/cbdba92a-a2da-4922-b9bf-f2e3e47a8048) |
|---|

| ![certificate_of_completion_statistics](https://github.com/user-attachments/assets/ea00e37b-403e-4429-bee6-64fb3c58c96f) |
|---|

| ![certificate_of_completion_git](https://github.com/user-attachments/assets/1beffa33-6eb1-4491-bd4d-74f06ab22da6) |
|---|

| ![certificate_of_completion_pandas](https://github.com/user-attachments/assets/8772b851-df59-4f81-922f-fac585167e9a) |
|---|

| ![certificate_of_completion_sql](https://github.com/user-attachments/assets/0e5cb029-60a6-4b73-aa75-cc3471043a7f) |
|---|

| ![certificate_of_completion_general_problem_solving_and_logical_reasoning](https://github.com/user-attachments/assets/001d5638-fe33-4efb-9834-c6883e88286c) |
|---|

| ![certificate_of_completion_dsa](https://github.com/user-attachments/assets/ac9f905c-4baf-43a3-acca-b8e84c1d0c95)|
|---|

| ![certificate_of_completion_accessibility](https://github.com/user-attachments/assets/be82a14a-d6c0-4812-9140-b0b69fbbb50d)|
|---|

| ![certificate_of_completion_cyber_security](https://github.com/user-attachments/assets/a99fab6c-4938-4115-83e1-9443b8094ffe) |
|---|

</div>

</details>

<div align="center">

![line](https://github.com/bylickilabs/bylickilabs/assets/109308073/bfd77a60-d426-4470-b417-fdbab0166188) 

</div>

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
start.bat
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

> Stored in local SQLite database per workspace.

---

## 🧩 Integration Targets
- Security Operation Centers (SOC)  
- Compliance & Audit Departments  
- Regulated industries (Finance, Energy, Government)  
- Data Protection & Forensics Teams  

---

## 🧪 API Certification & Testing
> SecureAI PolicyGuard includes automated **Schemathesis-based API certification tests** verifying OpenAPI 3.1 contract integrity.  
  - All test results are stored under `/tests/logs/` for compliance evidence.

---

## 🧠 Credits
> Developed by **Thorsten Bylicki**  
  - **BYLICKILABS – Intelligence Systems & Communications**  

---

## 📜 License
> © 2025 Thorsten Bylicki | BYLICKILABS
  - [LICENSE](LICENSE)
