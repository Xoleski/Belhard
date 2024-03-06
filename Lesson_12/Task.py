from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    TEXT,
    TIMESTAMP,
    ForeignKey,
    CheckConstraint,
    insert,
    create_engine,
    inspect,
    select
)

from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from enum import Enum

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

#
# class Base(DeclarativeBase):
#     ...
#
#
# class Projects(Base):
#     __tablename__ = "projects"
#     __table_args__ = (
#         CheckConstraint("length(name) >= 2"),
#     )
#
#     id = Column(INT, primary_key=True)
#     name = Column(VARCHAR(length=32), nullable=False, unique=True)
#
#     tasks = relationship(argument="Tasks", back_populates="projects")
#
#
# class UsersW(Base):
#     __tablename__ = "usersw"
#
#     id = Column(INT, primary_key=True)
#
#     tasks = relationship(argument="Tasks", back_populates="usersw")
#
#
# class StatusEnum(Enum):
#     done = "done"
#     not_done = "not_done"
#
#
# class Tasks(Base):
#     __tablename__ = "tasks"
#     __table_args__ = (
#         CheckConstraint("length(title) >= 2"),
#         CheckConstraint("length(description) >= 2"),
#         CheckConstraint("start_date < end_date")
#     )
#
#     id = Column(INT, primary_key=True)
#     title = Column(VARCHAR, nullable=False)
#     description = Column(TEXT)
#     start_date = Column(TIMESTAMP, nullable=False)
#     end_date = Column(TIMESTAMP, nullable=False)
#     status = Column(PgEnum(StatusEnum, name="order_status", create_type=False), nullable=False)
#     project_id = Column(INT, ForeignKey(column=Projects.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
#     executor_id = Column(INT, ForeignKey(column=UsersW.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
#
#     projects = relationship(argument=Projects, foreign_keys=[project_id], back_populates="tasks")
#     usersw = relationship(argument=UsersW, foreign_keys=[executor_id], back_populates="tasks")
#
#
# engine = create_engine(url="postgresql://user12:a0XCZnQ6H@217.76.60.77:6666/user12")
# session_maker = sessionmaker(bind=engine)

# with session_maker() as session:
#     response = session.scalars(statement=q)
#     print(response.unique().all())

# # stm = insert(UsersW).values(id=1)
# stm = select(UsersW)
# print(stm)


# author_id = Column(INT, ForeignKey(column=UsersW.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)



# from os import name
from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    TEXT,
    TIMESTAMP,
    ForeignKey,
    CheckConstraint,
    Enum,
    insert,
    create_engine,
    inspect,
    select,
    delete,
    update,
    insert
)

from sqlalchemy.dialects.postgresql import ENUM as PgEnum

# from enum import Enum

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Base(DeclarativeBase):
    ...


class Projects(Base):
    __tablename__ = "projects"
    __table_args__ = (
        CheckConstraint("length(name) >= 2"),
    )

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(length=32), nullable=False, unique=True)

    tasks = relationship(argument="Tasks", back_populates="projects")


class UsersW(Base):
    __tablename__ = "usersw"

    id = Column(INT, primary_key=True)

    tasks = relationship(argument="Tasks", back_populates="usersw")


# class StatusEnum(Enum):
#     done = "done"
#     not_done = "not_done"


class Tasks(Base):
    __tablename__ = "tasks"
    __table_args__ = (
        CheckConstraint("length(title) >= 2"),
        CheckConstraint("length(description) >= 2"),
        CheckConstraint("start_date < end_date")
    )

    id = Column(INT, primary_key=True)
    title = Column(VARCHAR, nullable=False)
    description = Column(TEXT)
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)
    status = Column(PgEnum(name="status", values=["done", "not_done"]))
    project_id = Column(INT, ForeignKey(column=Projects.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    executor_id = Column(INT, ForeignKey(column=UsersW.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

    projects = relationship(argument=Projects, foreign_keys=[project_id], back_populates="tasks")
    usersw = relationship(argument=UsersW, foreign_keys=[executor_id], back_populates="tasks")


engine = create_engine(url="postgresql://user12:a0XCZnQ6H@217.76.60.77:6666/user12")
session_maker = sessionmaker(bind=engine)

# print(Base.metadata.tables)
# print(Base.metadata.tables.usersw())

# print(Base.metadata.tables.update(UsersW))
# print(Base.metadata.tables.values())


# Base.metadata.create_all(bind=engine)

# Base.metadata.drop_all(bind=engine)

# АЛЕМБИК НУЖНО ПРОИНИЦИАЛИЗИРОВАТЬ
# ДЛЯ ЭТОГО В ТЕРМИНАЛЕЖ
# ALEMBIC INIT ALEMBIC<=это название папки, часто так и называется





# ВЫВОД ЗНАЧЕНИЙ В СТОЛБЦЕ
with session_maker() as session:
    response = session.get(entity=Tasks, ident=4)
    print(response.start_date)


# with session_maker() as session:
#     response = session.scalars(select(UsersW.id))
#     print([i for i in response])

# with session_maker() as session:
#     session.execute(insert(Projects).values(name='first'))
    # print(response)
# Base.metadata.tables.update(Projects, name('firts'))


# stm = insert(UsersW).values()
# # stm = select(UsersW)
# print(stm)


# author_id = Column(INT, ForeignKey(column=UsersW.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

from sqlalchemy.orm import selectinload, joinedload

q = select(Tasks).join(Projects)
q = q.filter(
    Tasks.status != "done"
    # Tasks.end_date <= "2024-03-06 00:00:00"
)

print(q)



# from psycopg2 import connect
# from psycopg2._psycopg import cursor
# from psycopg2.extras import NamedTupleCursor
#
# with connect(dsn="postgres://user12:a0XCZnQ6H@217.76.60.77:6666/user12", cursor_factory=NamedTupleCursor) as conn:
#     with conn.cursor() as cur: # type: cursor
#         # cur.execute("""
#         #     INSERT INTO projects (name) VALUES (%s), (%s), (%s)
#         # """, ("pj_1", "pj_2", "pj_3")
#         #     )
#
#         cur.execute("""
#             SELECT * FROM projects
#         """)
#         for result in cur:
#             print(result)
#
# with connect(dsn="postgres://user12:a0XCZnQ6H@217.76.60.77:6666/user12", cursor_factory=NamedTupleCursor) as conn:
#     with conn.cursor() as cur: # type: cursor
#         # cur.execute("""
#         #     INSERT INTO usersw (id) VALUES (%s), (%s), (%s)
#         # """, (1, 2, 3)
#         #     )
#
#         cur.execute("""
#             SELECT * FROM usersw
#         """)
#         for result in cur:
#             print(result)
#
#
# with connect(dsn="postgres://user12:a0XCZnQ6H@217.76.60.77:6666/user12", cursor_factory=NamedTupleCursor) as conn:
#     with conn.cursor() as cur: # type: cursor
#         # cur.execute("""
#         #     INSERT INTO tasks (title, description, start_date, end_date, project_id, executor_id) VALUES (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s)
#         # """, ("task_1", "dododo", "2024-03-01 00:00:00", "2024-03-03 00:00:00", 1, 1, "task_2", "lalala", "2024-02-01 00:00:00", "2024-03-17 00:00:00", 2, 2, "task_3", "bebebe", "2024-02-15 00:00:00", "2024-02-29 00:00:00", 3, 3)
#         #     )
#
#         # cur.execute("""
#         #     SELECT * FROM tasks
#         # """)
#
#         for result in cur:
#             print(result)





