def help(login_id,list_user):
    from src.F05 import custom_zip
    list_user = [[str(item) for item in row] for row in list_user]

    headers = list_user[0]
    data = []
    for i in range(1,len(list_user)):
        data.append(list_user[i])
    user_data = [dict(custom_zip(headers, row)) for row in data]
    user_data = [u for u in user_data if u['id'] == str(login_id)] # Filter username yang terlogin
    
    if not login_id: # Jika belum login
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.\n")
        print("Login: Masuk ke dalam akun yang sudah terdaftar\n")
        print("Register: Membuat akun baru\n")
        print("\nFootnote:")
        print("Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar\n")
        print("Jangan lupa untuk memasukkan input yang valid")
        return

    user_data = user_data[0]  # To select the user data dictionary
    
    role = str(user_data['role']).lower() # Mencari role user
    if role == 'agent':
        print("Halo Agent Purry. Kamu memanggil command HELP. \nKamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. \nBerikut adalah hal-hal yang dapat kamu lakukan sekarang:")
        print("Logout: Keluar dari akun yang sedang digunakan\n")
        print("Inventory: Melihat owca-dex yang dimiliki oleh Agent\n")
        # Add more commands or actions
        print("\nFootnote:")
        print("Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar\n")
        print("Jangan lupa untuk memasukkan input yang valid")
    elif role == 'admin':
        print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat lakukan:\n")
        print("Logout: Keluar dari akun yang sedang digunakan\n")
        print("Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent\n")
        # Add more commands or actions
        print("\nFootnote:")
        print("Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
        print("Jangan lupa untuk memasukkan input yang valid")
    else:
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print("Login: Masuk ke dalam akun yang sudah terdaftar")
        print("Register: Membuat akun baru")
        print("\nFootnote:")
        print("Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
        print("Jangan lupa untuk memasukkan input yang valid")

# Aplikasi fungsi help pada file main.py

# from src.F04 import help
# help(login_id,li_user)
