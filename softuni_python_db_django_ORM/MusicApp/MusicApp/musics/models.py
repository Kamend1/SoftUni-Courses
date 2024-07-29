from sqlalchemy import Column, Integer, String, Float, ForeignKey, CheckConstraint, LargeBinary
from sqlalchemy.orm import relationship, declarative_base

# Create your models here.
Base = declarative_base()


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    image_url = Column(String(255), nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    songs = relationship('Song', back_populates='album', cascade='all, delete-orphan')

    __table_args__ = (
        CheckConstraint('price >= 0', name='check_price_positive'),
    )


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    music_file_data = Column(LargeBinary, )
    album_id = Column(Integer, ForeignKey('albums.id'), nullable=False)
    album = relationship('Album', back_populates='songs')


from django.db import models

# Create your models here.
