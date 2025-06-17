def get_type_effectiveness(attacker_type, defender_type):
    effectiveness_chart = {
        ("Fire", "Grass"): 2,
        ("Water", "Fire"): 2,
        ("Electric", "Water"): 2,
        ("Grass", "Water"): 2,
    }
    return effectiveness_chart.get((attacker_type, defender_type), 1)
