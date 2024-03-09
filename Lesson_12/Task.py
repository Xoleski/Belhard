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

# from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from enum import IntEnum

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class TaskStatus(IntEnum):
    TODO: int = 1
    done: int = 2
    not_done: int = 3

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
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.TODO)
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





# # ВЫВОД ЗНАЧЕНИЙ В СТОЛБЦЕ
# with session_maker() as session:
#     response = session.get(entity=Tasks, ident=4)
#     print(response.start_date)





# with session_maker() as session:
    # session.execute(
    #     insert(UsersW).values([{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5},])
    # )
    # session.commit()

    # response = session.scalars(select(UsersW.id))
    # print("id: ", [i for i in response])
    # print(response)
#
# with session_maker() as session:
    # session.execute(
    #     insert(Projects).values([{"name": "pj_1"}, {"name": "pj_2"}, {"name": "pj_3"}, {"name": "pj_4"}])
    # )
    # session.commit()

    # response = session.scalars(select(Projects.id))
    # response_ = session.scalars(select(Projects.name))
    # for j in zip([i for i in response], [i for i in response_]):
    #     print("ID: ", j[0], "    NAME: ", j[1])

    # print([i for i in session.execute(select(Projects).union_all())])

from sqlalchemy import select,  delete, insert, and_, all_, or_, any_, func, Table, alias

with session_maker() as session:
    # session.execute(
    #     insert(Tasks).values([
    #         {"title": "first", "description": "jump", "start_date": "2024-03-01 00:00:00",
    #          "end_date": "2024-03-04 00:00:00", "status": TaskStatus.done, "project_id": 1, "executor_id": 1},
    #         {"title": "second", "description": "sleep", "start_date": "2024-03-06 00:00:00",
    #          "end_date": "2024-03-16 00:00:00", "status": TaskStatus.not_done, "project_id": 2, "executor_id": 2},
    #         {"title": "third", "description": "drink", "start_date": "2024-03-10 00:00:00",
    #          "end_date": "2024-03-15 00:00:00", "project_id": 3, "executor_id": 3},
    #         {"title": "fourth", "description": "rest", "start_date": "2024-03-02 00:00:00",
    #          "end_date": "2024-03-10 00:00:00", "status": TaskStatus.done, "project_id": 4, "executor_id": 4}
    #     ])
    # )
    # session.commit()
    #
    response = session.scalars(select(Tasks.id))
    response_ = session.scalars(select(Tasks.title))
    response_1 = session.scalars(select(Tasks.description))
    response_2 = session.scalars(select(Tasks.start_date))
    response_3 = session.scalars(select(Tasks.end_date))
    response_4 = session.scalars(select(Tasks.status))
    response_5 = session.scalars(select(Tasks.project_id))
    response_6 = session.scalars(select(Tasks.executor_id))

    for j in zip([i for i in response], [i for i in response_], [i for i in response_1], [i for i in response_2],
                 [i for i in response_3], [i for i in response_4], [i for i in response_5], [i for i in response_6]):
        print("ID: ", j[0], "    TITLE: ", j[1], "    DESCR: ", j[2], "    StDate: ", j[3], "    EndDate: ", j[4],
              "    STATUS: ", j[5], "    PJ_id: ", j[6], "    EXE_id: ", j[7])

from sqlalchemy.orm import selectinload, joinedload
    # j1 = session.scalars(select(Tasks.title).join(Projects))
# j1 = select(Tasks.title, Tasks.executor_id).join(UsersW)
#
# j1 = j1.filter(
#     or_(
#         Tasks.status != TaskStatus.done,
#         Tasks.end_date < func.now()
#     )
# )
# print(j1)

# for i in j1.fetch:
#     print(i)

# with session_maker() as session:
#     trtr = update(Tasks).where(Tasks.id == 8).values(end_date="2024-03-07 00:00:00")
#     session.execute(trtr)
#     session.commit()

with session_maker() as session:
    j1 = select(Tasks.title, UsersW.id, Projects.name).join(UsersW).join(Projects)

    j1 = j1.filter(
        and_(
            Tasks.status != TaskStatus.done,
            Tasks.end_date <= func.now()
        )
    )
    for i in session.execute(j1).unique():
        print(i)
#

# with session_maker() as session:
#     task = session.scalar(
#         select(Tasks)
#         .options(
#             joinedload(Tasks.usersw),
#             joinedload(Tasks.projects),
#
#         )
#
#     )
#     print(task.projects)








# with session_maker() as session:
#     resp = session.scalars(statement=j1)
#     print(resp)
#
    # for i in j1:
    #     gdg = session.get(entity=UsersW, ident=i)
    #     print(gdg.id)
#
#     j2 = session.scalars(j1)
#
#     print(session.get(entity=Projects, ident=i) for i in j1)

# with session_maker() as session:
#     session.execute(insert(Projects).values(name='first'))
    # print(response)
# Base.metadata.tables.update(Projects, name('firts'))


# stm = insert(UsersW).values()
# # stm = select(UsersW)
# print(stm)


# author_id = Column(INT, ForeignKey(column=UsersW.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

from sqlalchemy.orm import selectinload, joinedload

# q = select(Tasks).join(Projects)
# q = q.filter(
#     Tasks.status != "not_done"
#     # Tasks.end_date <= "2024-03-06 00:00:00"
# )
#
# print(q)



from psycopg2 import connect
from psycopg2._psycopg import cursor
from psycopg2.extras import NamedTupleCursor
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
# #         # cur.execute("""
# #         #     INSERT INTO tasks (title, description, start_date, end_date, project_id, executor_id) VALUES (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s)
# #         # """, ("task_1", "dododo", "2024-03-01 00:00:00", "2024-03-03 00:00:00", 1, 1, "task_2", "lalala", "2024-02-01 00:00:00", "2024-03-17 00:00:00", 2, 2, "task_3", "bebebe", "2024-02-15 00:00:00", "2024-02-29 00:00:00", 3, 3)
# #         #     )
# #
#         # cur.execute("""
#         #     INSERT INTO tasks (status) VALUES (%s)
#         # """, ("done", ))
#         #
#         cur.execute("""
#             SELECT * FROM projects
#         """)
#
#         for result in cur:
#             print(result)
        #




