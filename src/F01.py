def check_valid(username):
    acceptable_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")
    return all(char in acceptable_chars for char in username)

def register(list_user,list_monster,list_monster_inventory):
    from src.F05 import custom_zip
    from src.F05 import custom_isdigit
    list_user = [[str(item) for item in row] for row in list_user]
    list_monster = [[str(item) for item in row] for row in list_monster]
    list_monster_inventory = [[str(item) for item in row] for row in list_monster_inventory]

    headers = list_user[0]
    data = []
    for i in range(len(list_user)):
        if i > 0:
            data.append(list_user[i])
    user_data = [dict(custom_zip(headers, row)) for row in data]
    
    
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

    new_user_id = 1
    # User input for registration
    while True:
        username = input("Masukkan username: ")
        if not check_valid(username):
            print("Username hanya boleh mengandung huruf kapital/kecil, angka ,garis bawah _, dan garis hubung -")
            continue
        full = False
        for user in user_data:
            if user['username'] == username:
                print("Username sudah terdaftar! Silakan coba masukkan username lain")
                full = True
                continue
        if full:
                continue
        password = input("Masukkan password: ")
        for user in user_data:
            while user['id'] == str(new_user_id):
                new_user_id += 1
        break
    while True:
        print("Pilih monster sebagai monster awalmu:")
        for monster in monster_data:
            print(f"{monster['id']}. {monster['type']}")
        monster_benar = False
        selected_monster_id = input("Masukkan ID monster yang ingin dipilih: ")
        if not custom_isdigit(selected_monster_id):
            print("Masukkan format valid!")
            continue
        for monster in monster_data:
            if monster['id'] == str(selected_monster_id):
                monster_benar = True
        if not monster_benar:
            print("Monster ID tidak ada! Silakan masukkan ID monster yang tersedia.")
            continue
        new_user = {
            'id': str(new_user_id),
            'username': username,
            'password': password,
            'role' : 'agent',
            'oc': '0'
        }
        user_data.append(new_user)

        # Add selected monster to monster_inventory
        new_inventory = {
            'user_id': new_user_id,
            'monster_id': selected_monster_id,
            'level': '1'
        }
        monster_inventory.append(new_inventory)
        break

    # Write updated data
    headers = list(user_data[0].keys())
    list_user = [headers] + [[d[key] for key in headers] for d in user_data]

    headers = list(monster_inventory[0].keys())
    list_monster_inventory = [headers] + [[d[key] for key in headers] for d in monster_inventory]

    list_user = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_user]
    list_monster_inventory  = [[int(item) if custom_isdigit(item) else item for item in row] for row in list_monster_inventory]

    print(f"User {username} successfully registered with user ID {new_user_id} and selected monster ID {selected_monster_id}")
    return list_user,list_monster_inventory

# Call the register function to register a new user and update the monster inventory
# from src.F01 import register
# li_user,li_monster_inventory = register(li_user,li_monster,li_monster_inventory)
