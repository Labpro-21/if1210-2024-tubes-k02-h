def load():
    def csvtolist(csv_file, index_columnint): #index_columnint = index kolom yang bertipe data integer
        li, row, elmt = [], [], ''         
        with open(csv_file, 'r') as f:       
            for line in f:
                for i in line:
                    if i == ';':
                        row.append(elmt)
                        elmt = ''
                    elif i == '\n':
                        row.append(elmt)
                        li.append(row)
                        row, elmt = [], ''
                    else:
                        elmt += i
        for i in index_columnint: #mengubah kolom string menjadi int (sesuai tipe data kolom masing2)
            for j in range (1, len(li)):
                li[j][i] = int(li[j][i])

        return li
    
    import argparse, sys, os
    parser = argparse.ArgumentParser()
    parser.add_argument('folder')
    if len(sys.argv) != 2:
        print("\nTidak ada nama folder yang diberikan!\nUsage : python/py main.py <nama_folder>")
        sys.exit()
    else:
        args = parser.parse_args()
        path = 'data/' + args.folder #parent foldernya ./data (./data/folder/.csv), didalam folder data ada folder lagi baru kumpulan csv
        if not os.path.exists(path):
            print(f"\nFolder {args.folder} tidak ditemukan.")
            sys.exit()
        else: 
            print("\nLoading...\n")
            li_user = csvtolist((path + '/user.csv'), [0, 1, 2, 3, 4]) # Load semua header (id,username,password,role,oc)                          
            li_monster = csvtolist((path + '/monster.csv'), [0, 1, 2, 3, 4]) # Load semua header (id,type,atk_power,def_power.hp)             
            li_item_inventory = csvtolist((path + '/item_inventory.csv'), [0, 1, 2]) # Load semua header (user_id,type,quantity)                  
            li_monster_inventory = csvtolist((path + '/monster_inventory.csv'), [0, 1, 2])
            li_item_shop = csvtolist((path + '/item_shop.csv'), [0, 1, 2]) # load semua header (type,stock,price)
            li_monster_shop = csvtolist((path + '/monster_shop.csv'), [0, 1, 2])
            li_item = [['potion_id', 'type'], [1, 'strength'], [2, 'resilience'], [3, 'healing']]
            print("Selamat datang di program OWCA!")
            return li_user, li_monster, li_item, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop

#Aplikasi main.py        
#from src.F14_Load import load
#li_user, li_monster, li_item, li_item_inventory, li_monster_inventory, li_item_shop, li_monster_shop = load()

#saat menjalankan file main.py (langsung ketikkan di terminal)
#py main.py <nama_folder> atau python main.py <nama_folder>

#Catatan
#file csv disimpan didalam folder yang disimpan dalam parent folder data/ (saat menjalankan main.py, cukup ketikkan folder saja tanpa ./data/folder/.csv)
