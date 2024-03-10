from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    BOOLEAN,
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

from enum import IntEnum, Enum as SimpleEnum

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

from sqlalchemy import select,  delete, insert, and_, all_, or_, any_, func, Table, alias

from sqlalchemy.orm import selectinload, joinedload


class BloodType(IntEnum):
    BLANK: int = None
    I: int = 1
    II: int = 2
    III: int = 3
    IV: int = 4


class RhType(IntEnum):
    BLANK: int = None
    ZERO: int = 0
    PLUS: int = 1
    MINUS: int = 2


class Base(DeclarativeBase):
    ...


class Donor(Base):
    __tablename__ = "donor"
    __table_args__ = (
        CheckConstraint("length(name) > 2"),
    )

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(36))
    location = Column(VARCHAR(16))
    blood = Column(Enum(BloodType), nullable=False, default=BloodType.BLANK)
    rh = Column(Enum(RhType), nullable=False, default=RhType.BLANK)
    heart = Column(BOOLEAN, nullable=False, default=False)
    kidney_left = Column(BOOLEAN, nullable=False, default=False)
    kidney_right = Column(BOOLEAN, nullable=False, default=False)
    liver = Column(BOOLEAN, nullable=False, default=False)
    pancreas = Column(BOOLEAN, nullable=False, default=False)
    lung_left = Column(BOOLEAN, nullable=False, default=False)
    lung_right = Column(BOOLEAN, nullable=False, default=False)
    eyeball_left = Column(BOOLEAN, nullable=False, default=False)
    eyeball_right = Column(BOOLEAN, nullable=False, default=False)
    intestine = Column(BOOLEAN, nullable=False, default=False)
    tissues = Column(BOOLEAN, nullable=False, default=False)




class Departments(Base):
    __tablename__ = "departments"



# engine = create_engine(url="postgresql://user12:a0XCZnQ6H@217.76.60.77:6666/user12")
# session_maker = sessionmaker(bind=engine)

# with session_maker() as session:
#     ...
