def load(): #fungsi menerima dan cek apakah argumen valid lalu mengembalikan list-list berisi data csv
    def csvtolist(csv_file, listcolumn_int): #listcolumn_int = list kolom yang bertipe data integer
        list, row, elmt = [], [], ''         #cth list = [[B1K1, B1K2], [B2K1, B2K2]] (B = baris, K = kolom)
        with open(csv_file, 'r') as f:       #note: tipe data tiap kolom SUDAH disesuaikan
            for i in f.read():
                if i == ';':
                    row.append(elmt)
                    elmt = ''
                elif i == '\n':
                    row.append(elmt)
                    list.append(row)
                    row, elmt = [], ''
                else:
                    elmt += i

        for i in listcolumn_int: #mengubah tipe data kolom integer dari sebelumnya string
            for indeks in range (len(list)):
                if list[0][indeks] == i:
                    break
            for elmt in list[1:]:
                elmt[indeks] = int(elmt[indeks])
        return list
    
    import argparse, sys, os
    parser = argparse.ArgumentParser()
    parser.add_argument('folder')
    if len(sys.argv) != 2:
        print("\nTidak ada nama folder yang diberikan!\nUsage : python/py main.py/F14_Load.py <nama_folder>")
        sys.exit()
    else:
        args = parser.parse_args()
        path = 'data/' + args.folder #parent foldernya ./data
        if not os.path.exists(path):
            print(f"\nFolder {args.folder} tidak ditemukan.")
            sys.exit()
        else: 
            print("\nLoading...\n")
            list_user = csvtolist((path + '/user.csv'), ['id', 'oc'])                                                  #load masing-masing data csv ke masing-masing list 
            list_monster = csvtolist((path + '/monster.csv'), ['id', 'atk_power', 'def_power', 'hp'])                  #note: file .csv pasti tersedia
            list_item_inventory = csvtolist((path + '/item_inventory.csv'), ['user_id', 'quantity'])                   
            list_monster_inventory = csvtolist((path + '/monster_inventory.csv'), ['user_id', 'monster_id', 'level'])
            list_item_shop = csvtolist((path + '/item_shop.csv'), ['stock', 'price'])
            list_monster_shop = csvtolist((path + '/monster_shop.csv'), ['monster_id', 'stock', 'price'])
            print("Selamat datang di program OWCA!")
            return list_user, list_monster, list_item_inventory, list_monster_inventory, list_item_shop, list_monster_shop

list_user, list_monster, list_item_inventory, list_monster_inventory, list_item_shop, list_monster_shop = load() #note: nama list bisa disesuaikan