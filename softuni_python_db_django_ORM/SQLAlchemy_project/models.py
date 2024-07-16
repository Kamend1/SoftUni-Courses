from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from main import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User",)

Base.metadata.create_all(engine)
