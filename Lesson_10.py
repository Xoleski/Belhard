# модуль - это пайтон файл
# файл с модулями - это пакет

import sqlite3
from sqlite3 import connect

conn = connect("bd_1.db") # путь к БД
cur = conn.cursor() # курсор для совершения транзакций нужен
# у курсора есть методы: execut, executemany, ...
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR (32) NOT NULL DEFAULT ('Username') CHECK ( length(first_name) >= 2 ),
        email VARCHAR (128) NOT NULL UNIQUE CHECK ( length(email) >= 5 )
    );
""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS categ (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (16) NOT NULL UNIQUE CHECK (length(name) >= 2)
    );
""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS prod (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (128) NOT NULL UNIQUE CHECK (length(name) > 0),
        price decimal (8, 2) not null CHECK ( price > 0 ),
        is_published boolean not null default (false),
        categ_id INTEGER NOT NULL,
        FOREIGN KEY (categ_id) REFERENCES categ (id) ON DELETE RESTRICT
    );
""")
conn.commit()

cur.execute("""
    CREATE INDEX index_category_id ON products (categories_id)
""")

cur.execute("""
    CREATE INDEX index_is_published ON products (is_published)
""")



conn.close()

