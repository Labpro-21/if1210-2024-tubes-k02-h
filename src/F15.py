def save(li_user, li_monster, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop):
    import os

    def listtocsv(li_name, csv_file): #listtocsv mengubah list menjadi file .csv
        with open(csv_file, 'w') as f:
            line = ''
            for row in li_name:
                for index, elmt in enumerate(row):
                    if index == len(row)-1:
                        line += str(elmt)
                    else:
                        line += str(elmt) + ';'
                line += '\n'
            f.write(line)

    parentsave = 'data'
    path = parentsave + '/' + str(input("Masukkan nama folder: "))

    print("\nSaving...\n")

    if not os.path.exists(parentsave):
        os.makedirs(parentsave)
        print(f"Membuat folder {parentsave}...")

    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Membuat folder {path}...")

    listtocsv(li_user, (path + '/user.csv'))
    listtocsv(li_monster, (path + '/monster.csv'))
    listtocsv(li_item_inventory, (path + '/item_inventory.csv'))
    listtocsv(li_monster_inventory, (path + '/monster_inventory.csv'))
    listtocsv(li_item_shop, (path + '/item_shop.csv'))
    listtocsv(li_monster_shop, (path + '/monster_shop.csv'))

    print(f"Berhasil menyimpan data di folder {path}")

#Aplikasi main.py        
#from src.F14_Save import save
#save(li_user, li_monster, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop)

#Catatan
#file csv disimpan didalam folder yang disimpan dalam parent folder data/
