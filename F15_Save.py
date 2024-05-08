def save(list_user, list_monster, list_item_inventory, list_monster_inventory, list_item_shop, list_monster_shop): #parameter = nama setiap list
    import os

    def listtocsv(list_name, csv_file): #listtocsv mengubah list menjadi file .csv
        with open(csv_file, 'w') as f:
            x = ''
            for row in list_name:
                for elmt in row:
                    x += str(elmt) + ';'
                x = x.rstrip(';') + '\n'
            f.write(x.rstrip('\n'))

    parentsave = 'data'
    path = parentsave + '/' + str(input("Masukkan nama folder: "))

    print("\nSaving...\n")

    if not os.path.exists(parentsave):
        os.makedirs(parentsave)
        print(f"Membuat folder {parentsave}...")

    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Membuat folder {path}...")

    listtocsv(list_user, (path + '/user.csv'))
    listtocsv(list_monster, (path + '/monster.csv'))
    listtocsv(list_item_inventory, (path + '/item_inventory.csv'))
    listtocsv(list_monster_inventory, (path + '/monster_inventory.csv'))
    listtocsv(list_item_shop, (path + '/item_shop.csv'))
    listtocsv(list_monster_shop, (path + '/monster_shop.csv'))

    print(f"Berhasil menyimpan data di folder {path}")
