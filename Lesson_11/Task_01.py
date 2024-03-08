from psycopg2 import connect
from psycopg2._psycopg import cursor
from psycopg2.extras import NamedTupleCursor
#
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

        # cur.execute("""
        #     INSERT INTO departments (name) VALUES (%s), (%s), (%s), (%s)
        # """, ("DEP_1", "DEP_2", "DEP_3", "DEP_4")
        #     )

        # cur.execute("""
        #     INSERT INTO sub_departments (name) VALUES (%s), (%s), (%s), (%s)
        # """, ("SUB_1", "SUB_2", "SUB_3", "SUB_4")
        #     )


        # cur.execute("""
        #     INSERT INTO users (department_id, sub_department_id)
        #     VALUES (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s)
        # """, (9, 9, 9, 10, 10, None, None, 11, 12, 12)
        #     )
        #
        # conn.commit()

        # cur.execute("""
        #     INSERT INTO chats (name) VALUES (%s), (%s), (%s), (%s), (%s)
        # """, ("CH_1", "CH_2", "CH_3", "CH_4", "CH_5")
        #     )

        # cur.execute("""
        #     INSERT INTO chats_relations (chat_id, department_id, sub_department_id)
        #     VALUES (%s, %s, %s), (%s, %s, %s), (%s, %s, %s)
        # """, (1, 9, 10, 2, 9, 9, 3, 10, None)
        #     )
        #
        # conn.commit()

        #
        # cur.execute("""
        #     SELECT * FROM chats_relations
        # """)
        #
        # # conn.commit()
        #
        # for result in cur:
        #     print(result)

        # cur.execute("""
        #     SELECT chats_relations.chat_id as chat_id FROM chats_relations
        #     WHERE
        # """)

        # cur.execute("""
        #
        #     SELECT chats_relations.chat_id as chat_id
        #     FROM chats_relations INNER JOIN departments ON departments.id = chats_relations.department_id
        #     INNER JOIN sub_departments ON sub_departments.id = chats_relations.sub_department_id
        #     INNER JOIN chats ON chats.id = chats_relations.chat_id
        #
        # """)

        # cur.execute("""
        #
        #     SELECT chats.name as chat_name, users.id as user_id
        #
        #     FROM chats_relations
        #
        #     INNER JOIN departments ON departments.id = chats_relations.department_id
        #     INNER JOIN sub_departments ON sub_departments.id = chats_relations.sub_department_id
        #
        #     INNER JOIN chats ON chats.id = chats_relations.chat_id
        #     INNER JOIN users ON users.department_id = chats_relations.department_id AND users.sub_department_id = chats_relations.sub_department_id
        #
        #
        # """)


        #cur.execute("""

        #    SELECT chats.name as chat_name, users.id as user_id

          #  FROM chats_relations

          #  INNER JOIN departments ON departments.id = chats_relations.department_id
           # INNER JOIN sub_departments ON (sub_departments.id = chats_relations.sub_department_id OR chats_relations.sub_department_id IS NULL)

          #  INNER JOIN chats ON chats.id = chats_relations.chat_id
          #  INNER JOIN users ON users.department_id = chats_relations.department_id
          #      AND (users.sub_department_id = chats_relations.sub_department_id OR users.sub_department_id IS NULL)


      #  """)

        # cur.execute("""
        #
        #     SELECT chats.name as chat_name, users.id as user_id
        #
        #     FROM (
        #             SELECT *
        #             FROM chats_relations
        #             INNER JOIN departments ON departments.id = chats_relations.department_id
        #             LEFT JOIN sub_departments ON sub_departments.id = chats_relations.sub_department_id
        #             WHERE sub_departments.id IS NOT NULL
        #     ) filtered_chats_relations
        #
        #     INNER JOIN chats ON chats.id = filtered_chats_relations.chat_id
        #     INNER JOIN users ON users.department_id = filtered_chats_relations.department_id AND users.sub_department_id = filtered_chats_relations.sub_department_id
        #
        #
        # """)


        # conn.commit()

        # print(cur.fetchall())
        # #
        # cur.execute("""
        #     SELECT * FROM users
        # """)

        # # conn.commit()
        #

        # cur.execute("""

        #     SELECT chats.name as chat_name, users.id as user_id
        #     FROM (
        #             SELECT *
        #             FROM chats_relations
        #             INNER JOIN departments ON departments.id = chats_relations.department_id AND chats_relations.sub_department_id IS NULL

        #             UNION
        #             SELECT *
        #             FROM chats_relations
        #             INNER JOIN sub_departments ON sub_departments.id = chats_relations.sub_department_id AND chats_relations.department_id IS NULL

        #             UNION
        #             SELECT *
        #             FROM chats_relations
        #             INNER JOIN departments ON departments.id = chats_relations.department_id
        #             INNER JOIN sub_departments ON sub_departments.id = chats_relations.sub_department_id

        #             ) filtered_chats_relations
        #     INNER JOIN chats ON chats.id = filtered_chats_relations.chat_id
        #     INNER JOIN users ON users.department_id = filtered_chats_relations.department_id AND users.sub_department_id = filtered_chats_relations.sub_department_id

        # """)

        cur.execute("""

            SELECT chats.name as chat_name, users.id as user_id
            FROM chats_relations
            INNER JOIN departments ON departments.id = chats_relations.department_id AND chats_relations.sub_department_id IS NULL
            INNER JOIN chats ON chats.id = chats_relations.chat_id
            INNER JOIN users ON users.department_id = chats_relations.department_id
            UNION
            SELECT chats.name as chat_name, users.id as user_id
            FROM chats_relations
            INNER JOIN sub_departments ON sub_departments.id = chats_relations.sub_department_id AND chats_relations.department_id IS NULL
            INNER JOIN chats ON chats.id = chats_relations.chat_id
            INNER JOIN users ON users.department_id = chats_relations.department_id
            UNION
            SELECT chats.name as chat_name, users.id as user_id
            FROM chats_relations
            INNER JOIN departments ON departments.id = chats_relations.department_id
            INNER JOIN sub_departments ON sub_departments.id = chats_relations.sub_department_id
            INNER JOIN chats ON chats.id = chats_relations.chat_id
            INNER JOIN users ON users.department_id = chats_relations.department_id AND users.sub_department_id = chats_relations.sub_department_id

        """)



        # cur.execute("""
        #     SELECT chats.name FROM chats_relations
        #     JOIN chats ON chats.id = chats_relations.chat_id
        #     WHERE (chats_relations.sub_department_id IS NULL
        #         OR chats_relations.sub_department_id = (
        #             SELECT users.sub_department_id
        #             FROM users
        #             WHERE users.id = %(user_id)s)
        #     ) AND
        #         (chats_relations.department_id IS NULL
        #         OR chats_relations.department_id = (
        #             SELECT users.department_id
        #             FROM users
        #             WHERE users.id = %(user_id)s)
        #     );
        # """, ({"user_id": 3}))


        cur.execute("""
            SELECT chats.name FROM chats_relations
            JOIN chats ON chats.id = chats_relations.chat_id
            WHERE (chats_relations.sub_department_id IS NULL
                OR chats_relations.sub_department_id = (
                    SELECT users.sub_department_id
                    FROM users
                    WHERE users.id = %(user_id)s)
            ) AND
                (chats_relations.department_id IS NULL
                OR chats_relations.department_id = (
                    SELECT users.department_id
                    FROM users
                    WHERE users.id = %(user_id)s)
            );
        """, ({"user_id": 3}))

        for result in cur:
            print(result)



# print("7*8=", a := 7*8)





# ВТОРОЕ ЗАДАНИЕ


# with connect(dsn="postgres://user12:a0XCZnQ6H@217.76.60.77:6666/user12", cursor_factory=NamedTupleCursor) as conn:
#     with conn.cursor() as cur: # type: cursor
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS statuses(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(10) UNIQUE CHECK ( length(name) >= 2 )
        #     );
        # """)

        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS users_prod(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(24) CHECK ( length(name) >= 2 ),
        #         email VARCHAR(24) UNIQUE CHECK ( length(name) >= 2 )
        #     );
        # """)

        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS categories(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(24) UNIQUE CHECK ( length(name) >= 2 )
        #     );
        # """)

        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS orders(
        #         id SERIAL PRIMARY KEY,
        #         user_prod_id INTEGER,
        #         status_id INTEGER,
        #         FOREIGN KEY (user_prod_id) REFERENCES users_prod(id) ON DELETE RESTRICT ON UPDATE CASCADE,
        #         FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE RESTRICT ON UPDATE CASCADE
        #     );
        # """)

        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS products(
        #         id SERIAL PRIMARY KEY,
        #         title VARCHAR(36) CHECK ( length(title) >= 2 ),
        #         description VARCHAR(140) CHECK ( length(description) >= 2 ),
        #         category_id INTEGER,
        #         FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT ON UPDATE CASCADE
        #     );
        # """)

        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS order_items(
        #         id SERIAL PRIMARY KEY,
        #         order_id INTEGER,
        #         product_id INTEGER,
        #         FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE RESTRICT ON UPDATE CASCADE,
        #         FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT ON UPDATE CASCADE
        #     );
        # """)

        # conn.commit()

        # cur.execute("""
        #     SELECT * FROM users_prod
        # """)
        #
        # for result in cur:
        #     print(result)



