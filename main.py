from src.F00 import random_num
from src.F01 import register
from src.F02 import login
from src.F03 import logout
from src.F04 import help
from src.F07 import inventory
from src.F08 import battle
from src.F09 import arena
from src.F10 import shop
from src.F11 import laboratory
from src.F12 import shop_management
from src.F13 import monster_management
from src.F14 import load
from src.F15 import save
from src.F16 import exit_game

li_user, li_monster, li_item, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop = load()
login_id = "12345" # Asumsi user login

while True:
    if login_id:
        while True:
            a = input("inventory/battle/arena/shop/save/quit: ").lower()
            if a == 'inventory':
              inventory(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory)
            elif a == 'battle':
              li_user,li_monster,li_item_inventory,li_monster_inventory = battle(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory)
            elif a == 'arena':
              li_user,li_monster,li_item_inventory,li_monster_inventory = arena(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory)
            elif a == 'shop':
              li_user,li_monster,li_item_inventory,li_monster_inventory,li_item_shop,li_monster_shop = shop(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory,li_item_shop,li_monster_shop)
            elif a == 'save':
              save(li_user, li_monster, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop)
            elif a == 'quit':
              exit_game(li_user, li_monster, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop)
            else:
              continue
        break

    else:
        print("Silakan login dahulu")
        break
