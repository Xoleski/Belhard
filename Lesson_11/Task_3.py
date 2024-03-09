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

from enum import IntEnum

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

from sqlalchemy import select,  delete, insert, and_, all_, or_, any_, func, Table, alias

from sqlalchemy.orm import selectinload, joinedload


engine = create_engine(url="postgresql://user12:a0XCZnQ6H@217.76.60.77:6666/user12")
session_maker = sessionmaker(bind=engine)

with session_maker() as session:
    ...



