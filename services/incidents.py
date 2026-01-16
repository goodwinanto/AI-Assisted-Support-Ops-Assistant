import sqlite3
from datetime import datetime

DB = "incidents.db"

def save_incident(issue, severity, summary):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT,
        severity TEXT,
        created_at TEXT,
        ai_summary TEXT
    )
    """)

    cur.execute(
        "INSERT INTO incidents (issue, severity, created_at, ai_summary) VALUES (?, ?, ?, ?)",
        (issue, severity, datetime.now().isoformat(), summary)
    )

    conn.commit()
    conn.close()

def list_incidents():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT id, issue, severity, created_at FROM incidents")
    data = cur.fetchall()

    conn.close()
    return data
