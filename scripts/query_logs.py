import sqlite3
import sys

DB='logs.db'
conn=sqlite3.connect(DB)
cur=conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables=[t[0] for t in cur.fetchall()]
print('TABLES:', tables)
if 'query_logs' in tables:
    cur.execute("PRAGMA table_info(query_logs)")
    print('SCHEMA:', cur.fetchall())
    cur.execute("SELECT * FROM query_logs")
    rows=cur.fetchall()
    print('ROWS_COUNT:', len(rows))
    for r in rows:
        print(r)
else:
    print('TABLE `query_logs` does not exist in', DB)
conn.close()
