import os

def read_csv(file_name):
    data = []
    file_path = f"{file_name}.csv"  # Construct path directly

    if os.path.exists(file_path):
        with open(file_path, 'r') as csvfile:
            for line in csvfile:
                entry = []
                field = ""
                for char in line.strip():
                    if char != ";":
                        field += char
                    else:
                        entry.append(field)
                        field = ""
                entry.append(field)  # Add the last field
                data.append(entry)
    return data


def check_valid(username):
    acceptable_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")
    return all(char in acceptable_chars for char in username)


def register():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if not check_valid(username):
        print("Username tidak valid, hanya mengandung huruf, angka, _, dan -")
        return

    users_data = read_csv("user")
    for user in users_data:
        if user[1].lower() == username.lower():
            print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
            return


    id = len(users_data)
    coin = 0 

    with open('user.csv', 'a') as f:
        f.write(f"{id};{username};{password};agent;{coin}\n")

    print("Registrasi berhasil.")
    print("Silakan pilih salah satu monster sebagai monster awalmu.")
    print("1. Charizard")
    print("2. Bulbasaur")
    print("3. Aspal")

    monster_choice = input("\nMonster pilihanmu: ")
    monsters = {
        "1": "Charizard",
        "2": "Bulbasaur",
        "3": "Aspal",
    }
    monster = monsters.get(monster_choice, "Tidak ada monster")
    print(f"\nSelamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster}!")


register()
