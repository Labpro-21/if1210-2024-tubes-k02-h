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

def shop(login_id,list_user,list_monster,list_item_inventory,list_monster_inventory,list_item_shop,list_monster_shop):
    list_user = [[str(item) for item in row] for row in list_user]
    list_monster = [[str(item) for item in row] for row in list_monster]
    list_item_inventory = [[str(item) for item in row] for row in list_item_inventory]
    list_monster_inventory = [[str(item) for item in row] for row in list_monster_inventory]
    list_item_shop = [[str(item) for item in row] for row in list_item_shop]
    list_monster_shop = [[str(item) for item in row] for row in list_monster_shop]
    # Konversi 'List of List' ke 'List of Dict' untuk pemrosesan data
    headers = list_user[0]
    data = []
    for i in range(len(list_user)):
        if i > 0:
            data.append(list_user[i])
    user_data = [dict(custom_zip(headers, row)) for row in data]
    
    user_login = [u for u in user_data if u['id'] == str(login_id)]
    if not user_login:
        print("User_id tidak terdaftar!")
        list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
        list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
        list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
        list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
        list_item_shop = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_shop]
        list_monster_shop  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_shop]
        return list_user,list_monster,list_item_inventory,list_monster_inventory,list_item_shop,list_monster_shop
    user_login = user_login[0]
    role = str(user_login['role']).lower()
    if role != 'agent':
        print("Yah, hanya agent saja yang boleh masuk Shop and Currency.")
        list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
        list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
        list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
        list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
        list_item_shop = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_shop]
        list_monster_shop  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_shop]
        return list_user,list_monster,list_item_inventory,list_monster_inventory,list_item_shop,list_monster_shop
    
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

    headers = list_item_shop[0]
    data = []
    for i in range(len(list_item_shop)):
        if i > 0:
            data.append(list_item_shop[i])
    potion_shop = [dict(custom_zip(headers, row)) for row in data]

    headers = list_monster_shop[0]
    data = []
    for i in range(len(list_monster_shop)):
        if i > 0:
            data.append(list_monster_shop[i])
    monster_shop = [dict(custom_zip(headers, row)) for row in data]

    def display_shop_items(items):
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item}")

    # Iterasi Shop and Currency oleh User
    while True:
        print(">>> Selamat datang di Toko Mr. Yanto! Pilih aksi (beli/lihat/keluar):")
        action = input().lower()

        if action == "lihat":
            while True:
                print(">>> Mau lihat apa? (potion/monster):")
                item_type = input().lower()
                if item_type == "potion":
                    print("Potion yang tersedia: ")
                    display_shop_items([f"{potion['type']} (Stok: {potion['stock']}, Harga: {potion['price']} koin)" for potion in potion_shop])
                    break
                elif item_type == "monster":
                    print("Monster yang tersedia: ")
                    monster_shop_details = []
                    for monster in monster_shop:
                        monster_info = [m for m in monster_data if m['id'] == monster['monster_id']][0]
                        monster_shop_details.append(f"{monster['monster_id']}. {monster_info['type']} (ATK: {monster_info['atk_power']}, DEF: {monster_info['def_power']}, HP: {monster_info['hp']}, Stok: {monster['stock']}, Harga: {monster['price']} koin)")
                    display_shop_items(monster_shop_details)
                    break
                else:
                    continue

        elif action == "beli":
            user_id = str(login_id)
            print(f"Username Anda: {user_id}")
            while True:
                print(">>> Mau beli apa? (potion/monster):")
                item_type = input().lower()

                if item_type == "potion":
                    while True:
                        for user in user_data:
                            if user['id'] == user_id:
                                user_coins = int(user['oc'])
                        print(f"Jumlah koin Anda: {user['oc']}")
                        print("Potion yang dijual:")
                        display_shop_items([f"{potion['type']} (Stok: {potion['stock']}, Harga: {potion['price']} koin)" for potion in potion_shop])
    
                        print(">>> Pilih nomor urut potion yang ingin dibeli:")
                        idx = input()
                        if not custom_isdigit(idx):
                            print("Pilihan tidak valid. Silakan masukkan format yang benar.")
                            continue
                        selected_potion_idx = int(idx) - 1
                        if selected_potion_idx > len(potion_shop) - 1:
                            print("Pilihan tidak valid, silakan masukkan nomor pilihan yang tersedia")
                            continue
                        quantity = input("Masukkan banyaknya potion yang ingin dibeli: ")
                        if not custom_isdigit(quantity):
                            print("Pilihan tidak valid. Silakan masukkan format yang benar.")
                            continue
                        quantity = int(quantity)
                        selected_potion = potion_shop[selected_potion_idx]
                        if int(selected_potion['stock']) > 0 and int(selected_potion['stock']) - quantity >= 0:
                            for user in user_data:
                                if user['id'] == user_id:
                                    user_coins = int(user['oc'])
                                    if user_coins >= int(selected_potion['price']) * quantity:
                                        user_coins -= int(selected_potion['price']) * quantity
                                        selected_potion_name = selected_potion['type']
                                        user_potion = [p for p in potion_inventory if p['user_id'] == user_id and p['type'] == selected_potion_name]
                                        if user_potion:
                                            user_potion[0]['quantity'] = str(int(user_potion[0]['quantity']) + quantity)
                                        else:
                                            potion_inventory.append({'user_id': user_id, 'type': selected_potion_name, 'quantity': f'{quantity}'})
                                        selected_potion['stock'] = str(int(selected_potion['stock']) - quantity)
                                        user['oc'] = str(user_coins)
                                        print(f"Berhasil membeli {selected_potion_name}.")
                                    else:
                                        print("Koin Anda tidak mencukupi.")
                                    break
                            break

                        else:
                            print("Stok potion habis atau tidak mencukupi.")
                            break
                    break

                elif item_type == "monster":
                    for user in user_data:
                        if user['id'] == user_id:
                            user_coins = int(user['oc'])
                    print(f"Jumlah koin Anda: {user['oc']}")
                    print("Monster yang dijual:")
                    monster_shop_details = []
                    for monster in monster_shop:
                        monster_info = [m for m in monster_data if m['id'] == monster['monster_id']][0]
                        monster_shop_details.append(f"{monster['monster_id']}. {monster_info['type']} (ATK: {monster_info['atk_power']}, DEF: {monster_info['def_power']}, HP: {monster_info['hp']}, Stok: {monster['stock']}, Harga: {monster['price']} koin)")
                    display_shop_items(monster_shop_details)
                    while True:
                        print(">>> Pilih nomor urut monster yang ingin dibeli:")
                        idx = input()
                        if not custom_isdigit(idx):
                            print("Pilihan tidak valid. Silakan masukkan format yang benar.")
                            continue
                        selected_monster_idx = int(idx) - 1
                        if selected_monster_idx > len(monster_shop) - 1:
                            print("Pilihan tidak valid, silakan masukkan nomor pilihan yang tersedia")
                            continue
                        selected_monster = monster_shop[selected_monster_idx]
                        existing_monster = [m for m in monster_inventory if m['user_id'] == user_id and m['monster_id'] == selected_monster['monster_id']]
                        if int(selected_monster['stock']) > 0:
                            if existing_monster:
                                print("Anda sudah memiliki monster ini.")
                            else:
                                for user in user_data:
                                    if user['id'] == user_id:
                                        user_coins = int(user['oc'])
                                        if int(selected_monster['price']) < user_coins:
                                            user_coins -= int(selected_monster['price'])
                                            monster_inventory.append({'user_id': user_id, 'monster_id': selected_monster['monster_id'], 'level': '1'})
                                            selected_monster['stock'] = str(int(selected_monster['stock']) - 1)
                                            user['oc'] = str(user_coins)
                                            print("Berhasil membeli monster.")
                                        else:
                                            print("Koin tidak mencukupi.")
                                        break
                            break
                    break

                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    continue

        elif action == "keluar":
            print("Terima kasih telah berbelanja. Sampai jumpa lagi!")

            # Konversi balik ke List of List untuk menyimpan data
            headers = list(user_data[0].keys())
            list_user = [headers] + [[d[key] for key in headers] for d in user_data]

            headers = list(monster_data[0].keys())
            list_monster = [headers] + [[d[key] for key in headers] for d in monster_data]

            headers = list(potion_inventory[0].keys())
            list_item_inventory = [headers] + [[d[key] for key in headers] for d in potion_inventory]

            headers = list(monster_inventory[0].keys())
            list_monster_inventory = [headers] + [[d[key] for key in headers] for d in monster_inventory]

            headers = list(potion_shop[0].keys())
            list_item_shop = [headers] + [[d[key] for key in headers] for d in potion_shop]

            headers = list(monster_shop[0].keys())
            list_monster_shop = [headers] + [[d[key] for key in headers] for d in monster_shop]
            break
        else:
            continue
    list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
    list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
    list_item_inventory = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_inventory]
    list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
    list_item_shop = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_item_shop]
    list_monster_shop  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_shop]
    return list_user,list_monster,list_item_inventory,list_monster_inventory,list_item_shop,list_monster_shop

# APLIKASI FUNGSI shop() PADA main.py

# Asumsi list sudah diload dari CSV sebelumnya 

# list_user = [['id', 'username', 'password', 'role', 'oc'], ['12345', 'abc', 'koolabis', 'agent', '1500'], ['54321', 'def', 'rgerwfa', 'admin', '1500']]
# list_monster = [['id', 'type', 'atk_power', 'def_power', 'hp'], ['67890', 'pokemon', '200', '250', '500'], ['11111', 'pikachu', '245', '235', '245']]
# list_item_inventory = [['user_id', 'type', 'quantity'], ['12345', 'power', '1']]
# list_monster_inventory = [['user_id', 'monster_id', 'level'], ['12345', '67890', '1']]
# list_item_shop = [['type', 'stock', 'price'], ['power', '5', '100']]
# list_monster_shop = [['monster_id', 'stock', 'price'], ['67890', '5', '700'], ['11111', '5', '500']]

# Asumsi username sudah ada (user sudah login)

# from src.F10 import shop
# login_id = int(input())
# if login_id:
#     li_user,li_monster,li_item_inventory,li_monster_inventory,li_item_shop,li_monster_shop = shop(login_id,li_user,li_monster,li_item_inventory,li_monster_inventory,li_item_shop,li_monster_shop)
# else:
#     print("Anda belum login. Silakan login dahulu.")
