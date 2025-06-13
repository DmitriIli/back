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



metadata = MetaData()


class Base(DeclarativeBase):
    ...


# Base = declarative_base()
# mapper_registry = registry()


# class Users(Base):
#     __tablename__ = 'users'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(unique=True)
#     created_at: Mapped[datetime]
#     role: Mapped[int] = mapped_column(ForeignKey('roles.id'))
#     register_at: Mapped[TIMESTAMP] = mapped_column(
#         server_default=datetime.utcnow)


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