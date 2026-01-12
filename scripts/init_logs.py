import sqlite3

DB_PATH = 'logs.db'

schema = '''
CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    endpoint TEXT,
    question TEXT,
    response TEXT
);
'''

def init_db(path=DB_PATH):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.executescript(schema)
    conn.commit()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='requests'")
    exists = cur.fetchone() is not None
    conn.close()
    return exists

if __name__ == '__main__':
    ok = init_db()
    if ok:
        print(f"Initialized {DB_PATH} with table 'requests'.")
    else:
        print(f"Failed to initialize {DB_PATH}.")
