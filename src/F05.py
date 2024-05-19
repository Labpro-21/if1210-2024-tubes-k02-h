def maxi(a,b):
    if a > b:
        return a
    else:
        return b
    
def mini(a,b):
    if a < b:
        return a
    else:
        return b

def custom_zip(*args):
    def zipper(**attr):
        return attr
    iterators = [iter(iterable) for iterable in args]
    sentinel = zipper()
    
    while True:
        result = tuple(next(iterator, sentinel) for iterator in iterators)
        if any(val is sentinel for val in result):
            return
        yield result

def custom_isdigit(s):
    if isinstance(s, int):
        return True
    return all('0' <= char <= '9' for char in str(s))
    
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

def attack(attacker, defender): # Fungsi attack untuk F08
    from src.F00 import random_num
    n = random_num(-30, 30)  # Randomize n from -3 to 3
    atk_multiplier = 1 + n / 100
    attacker_atk_power = int(attacker['atk_power']) * atk_multiplier
    defender_def_power = mini(int(defender['def_power']), 50)  # Ensure def power does not exceed 50
    damage = int(attacker_atk_power * (1 - defender_def_power / 100))
    defender['hp'] = maxi(int(defender['hp']) - maxi(damage, 0), 0)  # Ensure damage is non-negative
    return attacker,defender

def attack_arena(attacker, defender): # Fungsi attack untuk F09
    from src.F00 import random_num
    n = random_num(-30, 30)  # Randomize n from -3 to 3
    atk_multiplier = 1 + n / 100
    attacker_atk_power = int(attacker['atk_power']) * atk_multiplier
    defender_def_power = mini(int(defender['def_power']), 50)  # Ensure def power does not exceed 50
    damage = int(attacker_atk_power * (1 - defender_def_power / 100))
    defender['hp'] = maxi(int(defender['hp']) - maxi(damage, 0), 0)  # Ensure damage is non-negative
    return attacker,defender,damage
