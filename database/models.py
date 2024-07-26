from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


import os
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(url=os.getenv("SQLALCHEMY_URL"))
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()
    weight: Mapped[float] = mapped_column()
    height: Mapped[float] = mapped_column()



class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

class Exercise(Base):
    __tablename__ = 'exercises'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(BigInteger)

class User_properties(Base):
    __tablename__ = "user_properties"

    tg_id = mapped_column(BigInteger)
    Hip:Mapped[float] = mapped_column()
    Hips:
