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
