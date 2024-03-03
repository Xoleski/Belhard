from psycopg2 import connect
from psycopg2._psycopg import cursor
from psycopg2.extras import NamedTupleCursor

with connect(dsn="postgres://user12:a0XCZnQ6H@217.76.60.77:6666/user12", cursor_factory=NamedTupleCursor) as conn:
    with conn.cursor() as cur: # type: cursor

        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS departments(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(32) NOT NULL UNIQUE CHECK ( length(name) >= 2 )
        #     );
        # """)
        #
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS sub_departments(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(32) NOT NULL CHECK ( length(name) >= 2 )
        #     );
        # """)
        #
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS users(
        #         id SERIAL PRIMARY KEY,
        #         department_id INTEGER,
        #         sub_department_id INTEGER,
        #         FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE RESTRICT ON UPDATE CASCADE,
        #         FOREIGN KEY (sub_department_id) REFERENCES sub_departments(id) ON DELETE RESTRICT ON UPDATE CASCADE
        #     );
        # """)
        #
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS chats(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(32) NOT NULL CHECK ( length(name) >= 2 )
        #     );
        # """)
        #
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS chats_relations(
        #         id SERIAL PRIMARY KEY,
        #         chat_id INTEGER NOT NULL,
        #         department_id INTEGER,
        #         sub_department_id INTEGER,
        #         FOREIGN kEY (chat_id) REFERENCES chats(id) ON DELETE RESTRICT ON UPDATE CASCADE,
        #         FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE RESTRICT ON UPDATE CASCADE,
        #         FOREIGN KEY (sub_department_id) REFERENCES sub_departments(id) ON DELETE RESTRICT ON UPDATE CASCADE
        #     );
        # """)
        #
        # conn.commit()

        # cur.execute("drop table chats_relations")
        # cur.execute("drop table chats")
        # cur.execute("drop table users")
        # cur.execute("drop table sub_departments")
        # cur.execute("drop table departments")
        # conn.commit()

        cur.execute("""
            I
        """)

