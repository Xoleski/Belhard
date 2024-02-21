# модуль - это пайтон файл
# файл с модулями - это пакет


from sqlite3 import connect

conn = connect("bd.sqlite3")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY
    );
""")
