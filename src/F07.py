def inventory(login_id,list_user,list_monster,list_item_inventory,list_monster_inventory):
    from src.F05 import custom_zip
    from src.F05 import custom_isdigit
    def display_shop_items(items):
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item}")
    list_user = [[str(item) for item in row] for row in list_user]
    list_monster = [[str(item) for item in row] for row in list_monster]
    list_item_inventory = [[str(item) for item in row] for row in list_item_inventory]
    list_monster_inventory = [[str(item) for item in row] for row in list_monster_inventory]

    headers = list_user[0]
    data = []
    for i in range(1,len(list_user)):
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
        print("Yah, hanya agent saja yang boleh masuk Inventory.")
        list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
        list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
        list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
        list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
        return list_user,list_monster,list_item_inventory,list_monster_inventory
    
    headers = list_monster[0]
    data = []
    for i in range(1,len(list_monster)):
        data.append(list_monster[i])
    monster_data = [dict(custom_zip(headers, row)) for row in data]
    
    headers = list_item_inventory[0]
    data = []
    for i in range(1,len(list_item_inventory)):
        data.append(list_item_inventory[i])
    potion_inventory = [dict(custom_zip(headers, row)) for row in data]

    headers = list_monster_inventory[0]
    data = []
    for i in range(1,len(list_monster_inventory)):
        data.append(list_monster_inventory[i])
    monster_inventory = [dict(custom_zip(headers, row)) for row in data]
    while True:
        print(f"Halo, user_id {login_id}, jumlah OWCA Coin Anda {user_login['oc']}")
        print(">>> Lihat Barang Apa? (potion/monster/quit):")
        item_type = input().lower()
        if item_type == "potion":
            print("Potion yang tersedia: ")
            potion_info = [f"Nama: {potion['type']}, Jumlah: {potion['quantity']}" for potion in potion_inventory if potion['user_id'] == str(login_id)]
            if potion_info:
                display_shop_items(potion_info)
            else:
                print("Anda tidak mempunyai potion apapun di inventory")
                continue
            print("Pilih nomor urut potion untuk informasi lebih lanjut: ")
            while True:
                idx = input()
                if not custom_isdigit(idx):
                    print("Pilihan tidak valid, silakan masukkan angka")
                    continue
                idx = int(idx) - 1
                if idx < 0 or idx > len(potion_info) - 1:
                    print("Pilihan tidak valid, silakan masukkan nomor yang tersedia")
                    continue
                selected_potion_info = potion_info[idx]
                print(f"{selected_potion_info}")
                break
        elif item_type == "monster":
            print("Monster yang tersedia: ")
            monster_inventory_details = []
            mns_info = []
            mns_inv = [monster_inventory[i] for i in range(len(monster_inventory)) if monster_inventory[i]['user_id'] == str(login_id)]
            for monster in mns_inv:
                monster_info = [m for m in monster_data if m['id'] == monster['monster_id']][0]
                monster_inventory_details.append(f"{monster['monster_id']}. {monster_info['type']}  (HP: {monster_info['hp']})")
                mns_info.append(f"{monster['monster_id']}. {monster_info['type']} (ATK: {monster_info['atk_power']}, DEF: {monster_info['def_power']}, HP: {monster_info['hp']})")
            display_shop_items(monster_inventory_details)
            print("Pilih nomor urut monster untuk informasi lebih lanjut: ")
            while True:
                idx = input()
                if not custom_isdigit(idx):
                    print("Pilihan tidak valid, silakan masukkan angka")
                    continue
                idx = int(idx) - 1
                if idx < 0 or idx > len(mns_info) - 1:
                    print("Pilihan tidak valid, silakan masukkan nomor yang tersedia")
                    continue
                selected_monster_info = mns_info[idx]
                print(f"{selected_monster_info}")
                break
        elif item_type == "quit":
            break
        else:
            continue
    return

# Aplikasi pada main.py

# Asumsi semua list telah diload

# from src.F07 import *
# login_id = str(input())
# if login_id:
#     inventory(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory)
# else:
#     print("Silakan login dahulu")
