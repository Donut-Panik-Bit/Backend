# pylint: disable=R0903
from sqlalchemy import CheckConstraint, Column, ForeignKey, MetaData
from sqlalchemy.dialects.postgresql import (
    BOOLEAN,
    CHAR,
    INTEGER,
    JSONB,
    TIMESTAMP,
    VARCHAR,
    FLOAT,
    TEXT
)
from sqlalchemy.orm import declarative_base
from enum import Enum
from app.db import convention


metadata = MetaData(naming_convention=convention)
DeclarativeBase = declarative_base(metadata=metadata)


class User_type(Enum):
    Admin = 1
    User = 2


class Users(DeclarativeBase):
    __tablename__ = "users"

    id = Column(
        "id", INTEGER, primary_key=True, unique=True, autoincrement=True, nullable=False
    )
    nickname = Column("nickname", VARCHAR(30), nullable=False, unique=True)
    name = Column("name", VARCHAR(15), nullable=False)
    user_type = Column("user_type", VARCHAR(15), nullable=False)
    surname = Column("surname", VARCHAR(20), nullable=False)
    phone = Column("phone", CHAR(12), nullable=False)


class Project(DeclarativeBase):
    __tablename__ = "project"

    id = Column(
        "id", INTEGER, primary_key=True, unique=True, autoincrement=True, nullable=False
    )
    author = Column(
        "author",
        VARCHAR(30),
        ForeignKey(Users.nickname, ondelete="CASCADE"),
        nullable=False,
    )
    brief_information = Column("brief_information", TEXT)
    descrip_problem = Column("descrip_problem", TEXT)
    primary_goal = Column("primary_goal", TEXT)
    major_groups = Column("major_groups", TEXT)
    implementation_experience = Column("implementation_experience", TEXT)
    project_potential = Column("project_potential", TEXT)
    status = Column("status", BOOLEAN, nullable=False)
