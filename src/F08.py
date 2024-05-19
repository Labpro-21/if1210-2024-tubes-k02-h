def battle(login_id,list_user,list_monster,list_item_inventory,list_monster_inventory):
    from time import sleep
    from src.F00 import random_num
    from src.F05 import adjust
    from src.F05 import attack
    from src.F05 import custom_zip
    from src.F05 import custom_isdigit
    from src.F06 import potion
    # Konversi List ke Dict
    list_user = [[str(item) for item in row] for row in list_user]
    list_monster = [[str(item) for item in row] for row in list_monster]
    list_item_inventory = [[str(item) for item in row] for row in list_item_inventory]
    list_monster_inventory = [[str(item) for item in row] for row in list_monster_inventory]

    headers = list_user[0]
    data = []
    for i in range(len(list_user)):
        if i > 0:
            data.append(list_user[i])
    user_data = [dict(custom_zip(headers, row)) for row in data]
    
    user_login = [u for u in user_data if u['id'] == str(login_id)]
    if user_login:
        user_login = user_login[0]
    else:
        print("User_id tidak terdaftar!")
        list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
        list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
        list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
        list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
        return list_user,list_monster,list_item_inventory,list_monster_inventory
    role = str(user_login['role']).lower()
    if role != 'agent':
        print("Yah, hanya agent saja yang boleh masuk Battle.")
        list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
        list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
        list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
        list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
        return list_user,list_monster,list_item_inventory,list_monster_inventory
    
    headers = list_monster[0]
    data = []
    for i in range(len(list_monster)):
        if i > 0:
            data.append(list_monster[i])
    monster_data = [dict(custom_zip(headers, row)) for row in data]
    
    headers = list_item_inventory[0]
    data = []
    for i in range(len(list_item_inventory)):
        if i > 0:
            data.append(list_item_inventory[i])
    potion_inventory = [dict(custom_zip(headers, row)) for row in data]

    headers = list_monster_inventory[0]
    data = []
    for i in range(len(list_monster_inventory)):
        if i > 0:
            data.append(list_monster_inventory[i])
    monster_inventory = [dict(custom_zip(headers, row)) for row in data]

    mns = []
    for monster_inv in monster_inventory:
        for monster_data_entry in monster_data:
            if monster_inv['monster_id'] == monster_data_entry['id']:
                monster = {**monster_data_entry, 'level': monster_inv['level']}  # Combining only the 'level' attribute
                monster = adjust(monster)  # Adjust monster attributes based on level
                mns.append(monster)
    
    opponent_idx = random_num(0,len(mns)-1)
    opponent_monster = mns[opponent_idx]
    opponent_monster['level'] = str(random_num(1, 5))
    opponent_monster = adjust(opponent_monster)
    sleep(1)
    print("\nMonster Lawan:")
    print("Nama: ", opponent_monster['type'])
    print("ATK Power: ", opponent_monster['atk_power'])
    print("DEF Power: ", opponent_monster['def_power'])
    print("HP: ", opponent_monster['hp'])
    print("Level: ", opponent_monster['level'])
    sleep(1)

    user_monsters = []
    for monster_inv in monster_inventory:
        for monster_data_entry in monster_data:
            if monster_inv['monster_id'] == monster_data_entry['id'] and monster_inv['user_id'] == login_id:
                monster = {**monster_data_entry, 'level': monster_inv['level']}  # Combining only the 'level' attribute
                monster = adjust(monster)  # Adjust monster attributes based on level
                user_monsters.append(monster)
    print("\nMonster Anda:")
    for idx, user_monster in enumerate(user_monsters):
        print(f"{idx + 1}. Name: {user_monster['type']} | ATK Power: {user_monster['atk_power']} | DEF Power: {user_monster['def_power']} | HP: {user_monster['hp']} | Level: {user_monster['level']}")
    
    user_choice = int(input("\nPilih monster untuk dipertarungkan: ")) - 1
    selected_user_monster = user_monsters[user_choice]
    print("\nAnda memilih:")
    print("Nama: ", selected_user_monster['type'])
    print("ATK Power: ", selected_user_monster['atk_power'])
    print("DEF Power: ", selected_user_monster['def_power'])
    print("HP: ", selected_user_monster['hp'])
    print("Level: ", selected_user_monster['level'])
    sleep(1)



    is_strength_used = False
    is_healing_used = False
    is_resilience_used = False
    user_quit = False
    ronde = 0
    while int(opponent_monster['hp']) > 0 and int(selected_user_monster['hp']) > 0:
        sleep(1)
        print(f"\nRONDE {ronde + 1}")
        sleep(1)
        print("\nGiliran Anda menyerang monster lawan!")
        sleep(1)
        action = input("Pilih aksi Anda - Attack, Potion, Quit: ")

        if action.lower() == 'attack':
            selected_user_monster,opponent_monster = attack(selected_user_monster, opponent_monster)
            print(f"{selected_user_monster['type']} menyerang monster {opponent_monster['type']}. HYAH!")
            sleep(1)
            print(f"MONSTER LAWAN ({opponent_monster['type']}): ")
            print(f"ATK Power: {opponent_monster['atk_power']}")
            print(f"DEF Power: {opponent_monster['def_power']}")
            print(f"HP: {opponent_monster['hp']}")
            print(f"Level: {opponent_monster['level']}")
            sleep(1)
            if opponent_monster['hp'] <= 0:
                break
        elif action.lower() == 'potion':
            print("\nPotion Tersedia:")
            user_potions = [potion for potion in potion_inventory if potion['user_id'] == login_id]
            if not user_potions:
                print("Anda tidak mempunyai potion apapun")
                continue
            for idx, user_potion in enumerate(user_potions):
                print(f"{idx + 1}. {user_potion['type']} - Quantity: {user_potion['quantity']}")
            potion_choice = int(input("\nPilih potion yang akan digunakan: ")) - 1
            selected_potion = user_potions[potion_choice]['type']

            if selected_potion == 'strength' and not is_strength_used:
                selected_user_monster,potion_inventory = potion(selected_potion, selected_user_monster, login_id, potion_inventory, monster_data)
                is_strength_used = True
            elif selected_potion == 'healing' and not is_healing_used:
                selected_user_monster,potion_inventory = potion(selected_potion, selected_user_monster, login_id, potion_inventory, monster_data)
                is_healing_used = True
            elif selected_potion == 'resilience' and not is_resilience_used:
                selected_user_monster,potion_inventory = potion(selected_potion, selected_user_monster, login_id, potion_inventory, monster_data)
                is_resilience_used = True
            else:
                print("You cannot use that potion again in this battle.")
            print("\nMonster Anda:")
            print("Name: ", selected_user_monster['type'])
            print("ATK Power: ", selected_user_monster['atk_power'])
            print("DEF Power: ", selected_user_monster['def_power'])
            print("HP: ", selected_user_monster['hp'])
            print("Level: ", selected_user_monster['level'])
            sleep(1)
            continue
        else:
            user_quit = True
            break
        if not user_quit:        
            print(f"Sekarang giliran monster {opponent_monster['type']} melawan monstermu! HYAH!")
            opponent_monster,selected_user_monster = attack(opponent_monster, selected_user_monster)
            sleep(1)
            print(f"MONSTER ANDA ({selected_user_monster['type']}): ")
            print(f"atk Power: {selected_user_monster['atk_power']}")
            print(f"def Power: {selected_user_monster['def_power']}")
            print(f"HP: {selected_user_monster['hp']}")
            print(f"Level: {selected_user_monster['level']}")
            sleep(1)
            if opponent_monster['hp'] <= 0:
                break
            else:
                ronde += 1
    if not user_quit:
        if opponent_monster['hp'] <= 0:
            oc_coin = random_num(10, 100)
            for user in user_data:
                if user['id'] == login_id:
                    user['oc'] = str(int(user['oc']) + oc_coin)
            print(f"Selamat, Anda Menang! Anda memperoleh {oc_coin} OC coins!")
            # Konversi balik ke List of List untuk menyimpan data
            headers = list(user_data[0].keys())
            list_user = [headers] + [[d[key] for key in headers] for d in user_data]

            headers = list(monster_data[0].keys())
            list_monster = [headers] + [[d[key] for key in headers] for d in monster_data]

            headers = list(potion_inventory[0].keys())
            list_item_inventory = [headers] + [[d[key] for key in headers] for d in potion_inventory]

            headers = list(monster_inventory[0].keys())
            list_monster_inventory = [headers] + [[d[key] for key in headers] for d in monster_inventory]

            list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
            list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
            list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
            list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]

            return list_user,list_monster,list_item_inventory,list_monster_inventory
        else:
            print("Yah, Anda dikalahkan monster lawan! Jangan menyerah, terus kembangkan monstermu!")
            list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
            list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
            list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
            list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
            return list_user,list_monster,list_item_inventory,list_monster_inventory
    else:
        print("Anda berhasil kabur dari pertarungan!")
        list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
        list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
        list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
        list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
        return list_user,list_monster,list_item_inventory,list_monster_inventory
    
# Aplikasi pada main.py

# Asumsi semua list telah diload sebelumnya

# list_user = [['id', 'username', 'password', 'role', 'oc'], ['12345', 'abc', 'koolabis', 'agent', '1500'], ['54321', 'aasd', 'rgerwfa', 'admin', '1500']]
# list_monster = [['id', 'type', 'atk_power', 'def_power', 'hp'], ['67890', 'pokemon', '200', '25', '500'], ['11111', 'pikachu', '245', '23', '245'], ['22222', 'charmander', '180', '20', '220'], ['33333', 'squirtle', '190', '22', '210'], ['44444', 'bulbasaur', '210', '19', '230'], ['55555', 'jigglypuff', '150', '18', '200'], ['66666', 'eevee', '170', '16', '190'], ['77777', 'snorlax', '250', '30', '350'], ['88888', 'gengar', '230', '10', '260']]
# list_item_inventory = [['user_id', 'type', 'quantity'], ['12345', 'strength', '5'], ['12345', 'healing', '5'], ['12345', 'resilience', '5']]
# list_monster_inventory = [['user_id', 'monster_id', 'level'], ['12345', '67890', '1'], ['12345', '55555', '2'], ['54321', '77777', '3']]

# Asumsi user sudah login (login_id terdefinisi sebagai sebuah string)
# File F08.py disimpan di folder src

# from src.F08 import *
# login_id = str(input())
# if login_id:
#     li_user,li_monster,li_item_inventory,li_monster_inventory = battle(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory)
# else:
#     print("Silakan login dahulu")
