def execute_turn(battle_id, attacker_monster, defender_monster, move):
    damage = calculate_damage(attacker_monster, defender_monster, move['power'], move['type_effectiveness'])
    defender_monster.health -= damage
    session.commit()
    return {"damage": damage, "defender_health": defender_monster.health}

def calculate_damage(attacker, defender, move_power, type_effectiveness):
    base_damage = (attacker.level * move_power) // defender.level
    return base_damage * type_effectiveness
