# models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float, Table, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# -- Players Table --
class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    money = Column(Integer, default=100)
    
    monsters = relationship("PlayerMonster", back_populates="player")
    battles = relationship("Battle", back_populates="player1", foreign_keys='Battle.player1_id')
    achievements = relationship("PlayerAchievement", back_populates="player")

# -- Monster Species (like Pokémon types) --
class MonsterSpecies(Base):
    __tablename__ = 'monster_species'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    type = Column(String)  # Fire, Water, Earth, Air, etc.
    base_stats = Column(JSON)  # {hp: 50, attack: 20, defense: 10}
    rarity = Column(String)  # Common, Rare, Epic, Legendary
    abilities = Column(JSON)  # List of moves/abilities

    monsters = relationship("PlayerMonster", back_populates="species")

# -- Player's Individual Monsters --
class PlayerMonster(Base):
    __tablename__ = 'player_monsters'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    species_id = Column(Integer, ForeignKey('monster_species.id'))
    
    nickname = Column(String)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    current_hp = Column(Integer)
    
    player = relationship("Player", back_populates="monsters")
    species = relationship("MonsterSpecies", back_populates="monsters")

# -- Battles (PvP or Wild) --
class Battle(Base):
    __tablename__ = 'battles'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'), nullable=True)
    winner_id = Column(Integer, ForeignKey('players.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_vs_ai = Column(Boolean, default=False)
    log = Column(JSON)  # Turn-by-turn history

    player1 = relationship("Player", foreign_keys=[player1_id], back_populates="battles")

# -- Trades --
class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    from_player_id = Column(Integer, ForeignKey('players.id'))
    to_player_id = Column(Integer, ForeignKey('players.id'))
    offered_monster_id = Column(Integer, ForeignKey('player_monsters.id'))
    requested_monster_id = Column(Integer, ForeignKey('player_monsters.id'))
    status = Column(String, default="pending")  # pending, accepted, rejected
    created_at = Column(DateTime, default=datetime.utcnow)

# -- Achievements --
class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)

# -- Player Achievements Progress --
class PlayerAchievement(Base):
    __tablename__ = 'player_achievements'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    achievement_id = Column(Integer, ForeignKey('achievements.id'))
    unlocked_at = Column(DateTime, default=datetime.utcnow)

    player = relationship("Player", back_populates="achievements")
