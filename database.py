# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Set up the database engine (SQLite file)
engine = create_engine("sqlite:///monster_game.db", echo=False)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Base class for ORM models
Base = declarative_base()

# Call this once to create tables
def create_tables():
    from models import Player, MonsterSpecies, PlayerMonster, Battle, Trade, Achievement, PlayerAchievement
    Base.metadata.create_all(engine)

