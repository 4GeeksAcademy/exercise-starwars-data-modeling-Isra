import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    favorites = relationship("Favorite")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    gender =Column(Enum('female', 'male', 'other', 'n/a'))
    birth_year = Column(Integer)
    height = Column(Integer)
    hair_color = Column(Enum('brown', 'blond', 'red', 'black', 'n/a'))
    eye_color = Column(Enum('brown', 'green', 'blue', 'gold', 'n/a'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet= relationship("Planet")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    population = Column(Integer)
    climate = Column(Enum('arid', 'temperate', 'tropical', 'frozen', 'murky'))
    terrain = Column(Enum('desert', 'grasslands', 'mountains', 'forests', 'rainforests','jungle', 'ocean', 'tundra','ice caves','ranges','swamps','gas gigant','lakes','grassy hills','cityscape'))
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    characters = relationship("Character")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name= Column(String(100), nullable=False)
    model= Column(String(100), nullable=False)
    vehicle_class=Column(Enum('repulsorcraft', 'wheeled', 'starfighter'))
    manufacturer= Column(Enum('Incom Corporation', 'Corellia Mining Corporation'), nullable=False)
    length= Column(Integer)
    passengers= Column(Integer)
    pilot_id= Column(Integer, ForeignKey('character.id'))
    character= relationship("Character")

class Favorites(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user= relationship("User")
    character= relationship("Character")
    planet= relationship("Planet")
    vehicle= relationship("Vehicle")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
