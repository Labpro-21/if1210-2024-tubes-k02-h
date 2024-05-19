def laboratory(login_id,list_user,list_monster,list_monster_inventory):
    from src.F05 import custom_isdigit
    from src.F05 import custom_zip
    list_user = [[str(item) for item in row] for row in list_user]
    list_monster = [[str(item) for item in row] for row in list_monster]
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
        list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
        return list_user,list_monster_inventory
    role = str(user_login['role']).lower()
    if role != 'agent':
        print("Yah, hanya agent saja yang boleh masuk Laboratory.")
        list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
        list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]
        return list_user,list_monster_inventory
    
    headers = list_monster[0]
    data = []
    for i in range(len(list_monster)):
        if i > 0:
            data.append(list_monster[i])
    monster_data = [dict(custom_zip(headers, row)) for row in data]

    headers = list_monster_inventory[0]
    data = []
    for i in range(len(list_monster_inventory)):
        if i > 0:
            data.append(list_monster_inventory[i])
    monster_inventory = [dict(custom_zip(headers, row)) for row in data]
    while True:
        # Menampilkan monster yang dimiliki agent
        print("============ MONSTER LIST ============")
        index = 1
        user_monsters = [monster for monster in monster_inventory if monster['user_id'] == login_id]
        for monster in user_monsters:
            monster_id = monster['monster_id']
            level = monster['level']

            # Mencari nama monster yang dimiliki
            monster_name = ""
            for monster in monster_data:
                if monster['id'] == monster_id:
                    monster_name = monster['type']
                    break
                
            # Menampilkan nama monster dan levelnya
            print(f"{index}. {monster_name} (Level: {level})")
            index += 1

        # Menampilkan daftar harga untuk upgrade
        print("\n============ UPGRADE PRICE ============")
        print("1. Level 1 -> Level 2: 300 OC")
        print("2. Level 2 -> Level 3: 500 OC")
        print("3. Level 3 -> Level 4: 800 OC")
        print("4. Level 4 -> Level 5: 1000 OC")

        # Meminta input pilihan monster
        monster_choice = (input(">>> Pilih monster: "))  
        if not custom_isdigit(monster_choice):
            print("Format tidak valid")
            continue
        monster_choice = int(monster_choice)

        # Cek Validasi
        if monster_choice < 1 or monster_choice > len(user_monsters):
            print("Pilihan monster tidak valid. Silakan pilih lagi.\n")
            continue

        # Mencari data monster yang dimiliki user
        selected_monster_data = user_monsters[monster_choice - 1]
        monster_id = selected_monster_data['monster_id']
        current_level = int(selected_monster_data['level'])

        # Menghitung biaya upgrade
        if current_level == 1: 
            upgrade_cost = 300
        elif current_level == 2:
            upgrade_cost = 500
        elif current_level == 3:
            upgrade_cost = 800
        elif current_level == 4:
            upgrade_cost = 1000
        elif current_level >= 5: 
            print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.\n")
            break

        # Memeriksa kembali data monster
        for monster in monster_data:
            if monster['id'] == monster_id:
                monster_name = monster['type']
                break
        print(f"\n{monster_name} akan di-upgrade ke level {current_level + 1}.")
        print(f"Harga untuk melakukan upgrade adalah {upgrade_cost} OC.")
        confirm = input(">>> Lanjutkan upgrade (Y/N): ").upper()

        # Memeriksa hasil konfirmasi
        if confirm == 'Y':
            for user in user_data:
                if user['id'] == login_id:
                    user_coins = int(user['oc'])
                    if int(user_coins) >= upgrade_cost:
                        # Proses transaksi
                        user_coins = str(int(user_coins) - upgrade_cost)
                        selected_monster_data['level'] = str(current_level + 1)
                        user['oc'] = user_coins
                        print(f"Selamat, {monster_name} berhasil di-upgrade ke level {selected_monster_data['level']}!")
                        print(f"Besar OC setelah upgrade: {user_coins}\n")
                    else:
                        print("Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.\n")
                    break
            break
        elif confirm == 'N':
            print("Upgrade dibatalkan.\n")
            break
        else:
            print("Input tidak valid. Upgrade dibatalkan.\n")
            break
    headers = list(user_data[0].keys())
    list_user = [headers] + [[d[key] for key in headers] for d in user_data]



    headers = list(monster_inventory[0].keys())
    list_monster_inventory = [headers] + [[d[key] for key in headers] for d in monster_inventory]

    list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
    list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]

    return list_user,list_monster_inventory

