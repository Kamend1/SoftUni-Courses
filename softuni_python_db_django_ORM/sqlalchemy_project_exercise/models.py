from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from main import engine

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    chef_id = Column(Integer, ForeignKey('chefs.id'))
    chef = relationship('Chef', back_populates='recipes')


class Chef(Base):
    __tablename__ = 'chefs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    recipes = relationship('Recipe', back_populates='chef')


Base.metadata.create_all(engine)
