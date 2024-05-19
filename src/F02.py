def login(list_user):
    username = input("Masukkan username: ")
    for i in range (1, len (list_user)):
        if username == list_user[i][1]:
            password = input("Masukkan password: ")
            if password == list_user[i][2]:
                print(f"Selamat datang {list_user[i][3]} {list_user[i][1]}")
                user_id = list_user[i][0]
                return user_id
            else:
                print("Password salah")
                break
        else:
            print("Username tidak terdaftar")
            break

# Aplikasi pada main.py

# from src.F02 import *
# login_id = login(li_user) # login_id dipakai sebagai variabel global di main.py untuk menentukan kepemilikan item, akses fungsi tertentu, dan status login user          
