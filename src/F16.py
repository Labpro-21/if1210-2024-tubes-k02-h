def exit_game(list_user, list_monster, list_item_inventory, list_monster_inventory, list_item_shop, list_monster_shop):
    from src.F15 import save
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
