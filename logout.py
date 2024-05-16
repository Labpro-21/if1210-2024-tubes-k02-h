def logout(user):
    if user['is_logged_in']:
        user['is_logged_in'] = False
        print(f"Pengguna {user['username']} telah logout.")
        user['username'] = None
    else:
        print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
