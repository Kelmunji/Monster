from models import Player, MonsterSpecies, PlayerMonster
from random import randint
from database import session

def catch_monster(player_id, species_id):
    # Simulate catch probability
    species = session.query(MonsterSpecies).get(species_id)
    catch_rate = calculate_catch_rate(species.rarity, player_level=5)  # Example with level 5
    if randint(1, 100) <= catch_rate:
        new_monster = PlayerMonster(player_id=player_id, species_id=species_id, level=1)
        session.add(new_monster)
        session.commit()
        return True
    return False

def calculate_catch_rate(rarity, player_level):
    # Simplified catch rate calculation
    if rarity == "common":
        return 50 + player_level
    elif rarity == "rare":
        return 30 + player_level
    return 10 + player_level

def level_up_monster(monster_id):
    monster = session.query(PlayerMonster).get(monster_id)
    monster.level += 1
    monster.health += 10  # Example of stat increase
    session.commit()
    return {"level": monster.level, "health": monster.health}
