import sqlite3
from pathlib import Path
from datetime import datetime

DB_NAME = "audit.db"
TABLE_NAME = "audit_log"


def init_db(base_dir: Path) -> sqlite3.Connection:
    db_dir = base_dir / ".secureai"
    db_dir.mkdir(parents=True, exist_ok=True)

    db_path = db_dir / DB_NAME
    conn = sqlite3.connect(db_path)

    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT NOT NULL,
            classification TEXT NOT NULL,
            action TEXT NOT NULL,
            risk_score INTEGER NOT NULL,
            entity_count INTEGER NOT NULL,
            explanation TEXT,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def log_action(
    conn: sqlite3.Connection,
    file_path: str,
    classification: str,
    action: str,
    risk_score: int,
    entity_count: int,
    explanation: str,
) -> None:
    try:
        conn.execute(
            f"""
            INSERT INTO {TABLE_NAME}
            (file_path, classification, action, risk_score, entity_count, explanation, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                file_path,
                classification,
                action,
                int(risk_score),
                int(entity_count),
                explanation,
                datetime.now().isoformat(timespec="seconds"),
            ),
        )
        conn.commit()
    except Exception as e:
        print(f"[ERROR] Failed to log audit entry: {e}")
