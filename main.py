from src.F01 import register
from src.F02 import login
from src.F03 import logout
from src.F04 import help
from src.F05 import custom_zip
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
login_id = None # Asumsi user login

while True:
  a = input("register/login/logout/help/inventory/battle/arena/shop/lab/shop_mgmt/monster_mgmt/save/quit: ").lower()
  if a == 'register':
    li_user,li_monster_inventory = register(li_user,li_monster,li_monster_inventory)
  elif a == 'login':
    login_id = str(login(login_id,li_user))
  elif a == 'logout':
    login_id = logout(login_id)
  elif a == 'help':
    help(login_id,li_user)
  elif a == 'inventory':
    inventory(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory)
  elif a == 'battle':
    li_user,li_monster,li_item_inventory,li_monster_inventory = battle(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory)
  elif a == 'arena':
    li_user,li_monster,li_item_inventory,li_monster_inventory = arena(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory)
  elif a == 'shop':
    li_user,li_monster,li_item_inventory,li_monster_inventory,li_item_shop,li_monster_shop = shop(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory,li_item_shop,li_monster_shop)
  elif a == 'lab':
    li_user,li_monster_inventory = laboratory(login_id,li_user,li_monster,li_monster_inventory)
  elif a == 'shop_mgmt':
    headers = li_user[0]
    data = []
    for i in range(1,len(li_user)):
      data.append(li_user[i])
    user_data = [dict(custom_zip(headers, row)) for row in data]
    if login_id:
      user_login = [u for u in user_data if u['id'] == int(login_id)]
      if user_login:
          user_login = user_login[0]
          role = str(user_login['role']).lower()
          if role != 'admin':
            print("Yah, hanya admin saja yang boleh masuk Shop Management.")
          else:
            li_monster, li_monster_shop, li_item_shop = shop_management(li_monster, li_item, li_monster_shop, li_item_shop)
    else:
        print("Anda belum login!")
  elif a =='monster_mgmt':
    headers = li_user[0]
    data = []
    for i in range(1,len(li_user)):
      data.append(li_user[i])
    user_data = [dict(custom_zip(headers, row)) for row in data]
    if login_id:
      user_login = [u for u in user_data if u['id'] == int(login_id)]
      if user_login:
          user_login = user_login[0]
          role = str(user_login['role']).lower()
          if role != 'admin':
            print("Yah, hanya admin saja yang boleh masuk Monster Management.")
          else:
            li_monster = monster_management(li_monster)
    else:
        print("Anda belum login!")
  elif a == 'save':
    save(li_user, li_monster, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop)
  elif a == 'quit' or a == 'exit':
    exit_game(li_user, li_monster, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop)
  else:
    continue

