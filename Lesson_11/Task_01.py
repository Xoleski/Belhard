from psycopg2 import connect
from psycopg2._psycopg import cursor
from psycopg2.extras import NamedTupleCursor

with connect(dsn="postgres://user12:a0XCZnQ6H@217.76.60.77:6666/user12", cursor_factory=NamedTupleCursor) as conn:
    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE IF NOT EXIST departments(
            id SERIAL NOT NULL PRIMARY KEY,
            name VARCHAR(32) NOT NULL UNIQUE CHECK ( length(name) >= 2 )
            )
            
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXIST users(
            id SERIAL NOT NULL PRIMARY KEY,
            FOREIGN KEY (department_id) REFERENCE departments(id) ON DELETE RESTRICT ON UPDATE CASCADE, 
            FOREIGN KEY (sub_department_id)
            )
        """)



