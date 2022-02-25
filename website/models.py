from sqlalchemy import ForeignKey, Integer
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(150), unique=True)
    teams = db.relationship('Team')

class Character(db.model):
    id = db.Column(db.interger, primary_key=True)
    name = db.Column(db.String(12), unique=True)
    franchise_id = db.relationship('Franchise')

class Team(db.model):
    id = db.Column(db.integer, primary_key=True)
    user = db.relationship('User')
    character = db.relationship('Character')

class Franchise(db.model):
    id = db.column(db.interger, primary_key=True)
    name = db.column(db.string, unique=True)

class Team_Pair(db.model):
    id = db.column(db.integer, primary_key=True)
    trainer_id = db.relationship('Trainer')
    pokemon_id = db.relaitonship('Pokemon')
    # Not sure if this will actually establish the many to many relationship

class Pokemon(db.model):
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(12), unique=True)
    type = db.column(db.string(12))
    level = db.column(db.intger)
    trainer = db.relationship('Team_Pair')

class Pokemon_type(db.model):
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(12, unique=True))
