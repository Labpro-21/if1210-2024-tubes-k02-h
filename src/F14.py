import os
def custom_split(text, delimiter=','):
    result = []
    current_word = ''
    inside_quotes = False

    for char in text:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == delimiter and not inside_quotes:
            result.append(current_word)
            current_word = ''
        else:
            current_word += char

    result.append(current_word)

    return result
# Load data from CSV files
def load(file):
    data = []
    with open(file, 'r') as f:
        header = custom_split(f.readline().strip(), ',')  # Read the header
        for line in f:
            values = custom_split(line.strip(), ',')
            row = {header[i]: values[i] for i in range(len(header))}
            data.append(row)
    headers = list(data[0].keys())
    arr = [headers] + [[d[key] for key in headers] for d in data]
    return arr

# Agar berjalan baik, F14.py harus diletakkan di folder src, sedangkan file CSV disimpan di folder data

# Aplikasi pada main.py

# from src.F14 import load
# list_user = load('./data/user.csv')
# list_monster = load('./data/monster.csv')
# list_item_inventory = load('./data/item_inventory.csv')
# list_monster_inventory = load('./data/monster_inventory.csv')
# list_item_shop = load('./data/item_shop.csv')
# list_monster_shop = load('./data/monster_shop.csv')