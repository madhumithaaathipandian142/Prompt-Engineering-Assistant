import sqlite3
import csv
import io
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "prompt_history.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                feature TEXT NOT NULL,
                input_text TEXT NOT NULL,
                prompt_text TEXT NOT NULL,
                response_text TEXT
            )
        """)

def save_record(feature, input_text, prompt_text, response_text=""):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO history (created_at, feature, input_text, prompt_text, response_text) VALUES (?, ?, ?, ?, ?)",
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), feature, input_text, prompt_text, response_text)
        )

def get_history(limit=100):
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM history ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
        return [dict(row) for row in rows]

def clear_history():
    with get_connection() as conn:
        conn.execute("DELETE FROM history")

def history_as_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["created_at", "feature", "input_text", "prompt_text", "response_text"])
    for row in get_history(limit=10000):
        writer.writerow([row["created_at"], row["feature"], row["input_text"], row["prompt_text"], row["response_text"]])
    return output.getvalue()
