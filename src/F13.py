# Function for managing monsters (viewing, adding, deleting) with validation
def monster_management(list_monster):
    from src.F05 import custom_isdigit
    from src.F05 import custom_zip
    list_monster = [[str(item) for item in row] for row in list_monster]

    headers = list_monster[0]
    data = []
    for i in range(len(list_monster)):
        if i > 0:
            data.append(list_monster[i])
    monster_data = [dict(custom_zip(headers, row)) for row in data]

    while True:
        print("\nMonster Management Menu:")
        print("1. Tampilkan semua monster")
        print("2. Tambahkan monster baru")
        print("3. Keluar\n")
        choice = input("Masukkan pilihan (1, 2, or 3): ")
        if choice == "1":  # View all monsters
            print("Semua Monster:")
            for monster in monster_data:
                print(f"{monster['id']}. {monster['type']} (ATK: {monster['atk_power']}, DEF: {monster['def_power']}, HP: {monster['hp']})")
            continue
        elif choice == "2":  # Add a new monster
            new_monster_name = input("Masukkan nama monster baru: ")

            # Check if the new monster_name already exists in monster_data
            monster_full = False
            for monster in monster_data:
                if monster['type'] == new_monster_name:
                    print("Monster ini sudah tersedia di menu. Silakan masukkan nama yang berbeda.\n")
                    monster_full = True
            if monster_full:
                continue

            # Collect other monster details
            new_monster_id = 1
            for monster in monster_data:
                if monster['id'] == str(new_monster_id):
                    new_monster_id += 1

            new_hp = input("Masukkan hit points (integer positif): ")
            new_attack_power = input("Masukkan attack power (integer positif): ")
            new_defence_power = input("Masukkan defence power (integer 1-50): ")
            
            if custom_isdigit(new_attack_power) and custom_isdigit(new_defence_power) and custom_isdigit(new_hp):
                new_hp = int(new_hp)
                new_attack_power = int(new_attack_power)
                new_defence_power = int(new_defence_power)
                if not (0 < new_defence_power <= 50):
                    print("Defence power harus di dalam rentang 1-50")
                    continue
                if new_hp <= 0 and new_attack_power <= 0 and new_defence_power <= 0:
                    print("Masukan harus bilangan bulat positif!")
                    continue
            else:
                print("Silakan masukkan format yang benar!")
                continue

            new_monster = {
                'id': str(new_monster_id),
                'type': str(new_monster_name),
                'atk_power': str(new_attack_power),
                'def_power': str(new_defence_power),
                'hp': str(new_hp)        
                }
            monster_data.append(new_monster)
            print("Monster baru berhasil ditambahkan.")
            continue
        elif choice == "3":
            print("Menutup monster management...")
            headers = list(monster_data[0].keys())
            list_monster = [headers] + [[d[key] for key in headers] for d in monster_data]
            list_monster = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster]
            return list_monster
        else:
            print("Silakan masukkan pilihan yang tersedia")
            continue

# from src.F13 import monster_management
# li_monster = monster_management(li_monster)