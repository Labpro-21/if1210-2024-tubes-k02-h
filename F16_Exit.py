def exit_game():
    from F15_Save import save
    global list_user
    global list_monster
    global list_item_inventory
    global list_monster_inventory
    global list_item_shop
    global list_monster_shop
    while True:
        user_input = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
        if user_input == 'y':
            # Menjalankan prosedur save
            save(list_user, list_monster, list_item_inventory, list_monster_inventory, list_item_shop, list_monster_shop)
            exit()
        elif user_input == 'n':
            # Keluar program
            exit()
        else:
            continue
