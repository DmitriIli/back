from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, JSON, DateTime, Numeric, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, DeclarativeMeta, registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from typing import List,  Annotated
from datetime import datetime
from enum import Enum

metadata_obj = MetaData()

# users_table = Table(
#     'users',
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('name', String, unique=True)
# )


class Base(DeclarativeBase):
    ...


intpk = Annotated[int, mapped_column(int, primary_key=True)]


class Roles(Enum):
    user = 'user'
    admin = 'admin'


class Users(Base):
    __tablename__ = 'users'
    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    role: Mapped[Roles]


class Notes(Base):
    __tablename__ = 'notes'
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    content: Mapped[str]
    date_time: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class Events(Base):
    __tablename__ = 'events'
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str]
    description: Mapped[str]
    date_time: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    

class Tags(Base):
    __tablename__ = 'tags'
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str] = mapped_column(unique=True)


# class Roles(Base):
#     __tablename__ = 'roles'
#     id: Mapped[intpk]
#     role = Mapped[Roles]
#     description: Mapped[str]


