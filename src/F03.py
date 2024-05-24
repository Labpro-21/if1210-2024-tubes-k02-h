def logout(login_id):
    if login_id:
        print("Kamu telah logout")
        return None
    else:
        print("Tidak bisa logout karena kamu belum login")
        return

# Aplikasi pada main.py

# from src.F03 import *
# login_id = logout(login_id) # login_id dipakai sebagai variabel global di main.py untuk menentukan kepemilikan item, akses fungsi tertentu, dan status login user          