from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, JSON, DateTime, Numeric, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, DeclarativeMeta, registry
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from datetime import datetime

metadata_obj = MetaData()

users_table = Table(
    'users',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String, unique=True)
)

class Base(DeclarativeBase):
    ...



class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True,nullable=False)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
    # role: Mapped[int] = mapped_column(ForeignKey('roles.id'))

   
class Notes(Base):
    __tablename__ = 'notes'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    content: Mapped[str]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

class Events(Base):
    __tablename__= 'events'
    id: Mapped[int] = mapped_column(primary_key=True)


# class Roles(Base):
#     __tablename__ = 'roles'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     description: Mapped[str]


# class Notes(Base):
#     __tablename__ = 'notes'
#     id: Mapped[int] = mapped_column(primary_name=True)
#     user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
#     title: Mapped[str]
#     data: Mapped[DateTime]
#     interval: Mapped[interval] = mapped_column(unique=True)
#     category: Mapped[category]
#     create_on: Mapped[DateTime] = mapped_column(default=datetime.now())