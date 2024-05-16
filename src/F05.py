def adjust(monster):
    level = int(monster['level'])
    if level == 1:
        return monster
    else:
        factor = 1 + (int(level) - 1) * 0.1
        monster['atk_power'] = int(int(monster['atk_power']) * factor)
        monster['def_power'] = int(int(monster['def_power']) * factor)
        monster['hp'] = int(int(monster['hp']) * factor)
        return monster

def attack(attacker, defender):
    from src.F00 import random_num
    n = random_num(-30, 30)  # Randomize n from -3 to 3
    atk_multiplier = 1 + n / 100
    attacker_atk_power = int(attacker['atk_power']) * atk_multiplier
    defender_def_power = min(int(defender['def_power']), 50)  # Ensure def power does not exceed 50
    damage = int(attacker_atk_power * (1 - defender_def_power / 100))
    defender['hp'] = max(int(defender['hp']) - max(damage, 0), 0)  # Ensure damage is non-negative
    return attacker,defender
