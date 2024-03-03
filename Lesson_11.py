from psycopg2 import connect
from psycopg2._psycopg import cursor
from psycopg2.extras import NamedTupleCursor

with connect(dsn= "postgres://user12:a0XCZnQ6H@217.76.60.77:6666/user12", cursor_factory=NamedTupleCursor) as conn:
    with conn.cursor() as cur: # type: cursor
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS tags(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(16) NOT NULL UNIQUE CHECK ( length(name) >= 2 )
        #     );
        # """)
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS topics(
        #         id SERIAL PRIMARY KEY,
        #         title VARCHAR(128) NOT NULL CHECK ( length(title) >= 2 ),
        #         body TEXT NOT NULL,
        #         date_created TIMESTAMP NOT NULL DEFAULT (now()),
        #         is_published BOOLEAN NOT NULL DEFAULT (false)
        #     );
        # """)
        # cur.execute("""
        #         CREATE TABLE IF NOT EXISTS topic_tags(
        #         tag_id INTEGER,
        #         topic_id INTEGER,
        #         PRIMARY KEY (tag_id, topic_id),
        #         FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE RESTRICT ON UPDATE CASCADE,
        #         FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE RESTRICT ON UPDATE CASCADE
        #     );
        # """)
        # conn.commit()

        # cur.execute("""
        #     INSERT INTO tags (name) VALUES (%s);
        # """, ("MOTO", ))
        # conn.commit()

        # cur.execute("""
        #     SELECT * FROM tags;
        # """)

        # print(cur.fetchall())

        # for result in cur:
        #     print(result.name)

        # Выборка с условием
        # cur.execute("""
        #     SELECT * FROM tags WHERE tags.id >= %s;
        # """, (2, ))


        cur.execute("""
            SELECT tags.name as tag_name, topics.title as topic_title
            FROM tags INNER JOIN topic_tags ON tags_id = topic_tags tag_id
            INNER JOIN topics ON topics_tags.topic_id = topic.id
            WHERE topics.is_published = true;
        """)

        print(cur.fetchall())
