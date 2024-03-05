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
    inspect
)

from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from enum import Enum

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


class Users(Base):
    __tablename__ = "users"

    id = Column(INT, primary_key=True)

    tasks = relationship(argument="Tasks", back_populates="users")


class StatusEnum(Enum):
    done = "done"
    not_done = "not_done"


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
    status = Column(PgEnum(StatusEnum, name="order_status", create_type=False), nullable=False)
    project_id = Column(INT, ForeignKey(column=Projects.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    author_id = Column(INT, ForeignKey(column=Users.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    executor_id = Column(INT, ForeignKey(column=Users.id, ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

    projects = relationship(argument=Projects, foreign_keys=[project_id], back_populates="tasks")
    users = relationship(argument=Users, foreign_keys=[author_id, executor_id], back_populates="tasks")


engine = create_engine(url="postgresql://user12:a0XCZnQ6H@217.76.60.77:6666/user12")
session_maker = sessionmaker(bind=engine)



