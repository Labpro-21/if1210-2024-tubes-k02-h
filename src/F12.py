#fungsi illegal: pop, slicing
#ubah nama loadshop, ubah isPInt, 0 add, 0 change, 0 delete, tli_potion -> tli_item, none = loadtlinot, tambah, ubah, hapus
def shop_management(li_monster, li_item, li_monster_shop, li_item_shop): #yang bisa masuk pasti rolenya admin
    def load_tli(li_monster, li_item, li_monster_shop, li_item_shop):
        def capital(string): #kapital huruf pertama
            if ord(string[0]) in range (97, 123):
                capital_string = string[0].upper()
                for i in range (1, len(string)):
                    capital_string += string[i]
                return capital_string
            else:
                return string

        def pops(li, index): #index start 0
            result = []
            for idx, elmt in enumerate (li):
                if idx != index:
                    result.append(elmt)
            return result
        
        def findrow(elmt, index_column, li): #cari index row, index_column start 0
            for index, row in enumerate (li):
                if row[index_column] == elmt:
                    return index

        tli_monster = [['ID', 'Type', 'ATK Power', 'DEF Power', 'HP', 'Stock', 'Price']] #tli_monster = list untuk table monster (gabungan list)
        for index, row in enumerate (li_monster_shop):
            if index != 0: #exclude row pertama (column)
                tli_monster.append(li_monster[findrow(row[0], 0, li_monster)] + pops(row, 0))

        tli_item = [['ID', 'Type', 'Stok', 'Harga']] #tli_item = list untuk table item (gabungan list)
        for index, row in enumerate (li_item_shop):
            if index != 0: #exclude row pertama (column)
                id = pops(li_item[findrow(row[0], 1, li_item)], 1)
                tli_item.append(id + row)
        for index, row in enumerate (tli_item):
            if index != 0:
                row[1] = capital(row[1]) + ' Potion'
        
        return tli_monster, tli_item

    def load_tlinot(li_monster, li_item, li_monster_shop, li_item_shop):
        def capital(string): #kapital huruf pertama
            if ord(string[0]) in range (97, 123):
                capital_string = string[0].upper()
                for i in range (1, len(string)):
                    capital_string += string[i]
                return capital_string
            else:
                return string
            
        def findrow(elmt, index_column, li): #cari index row, index_column start 0
            for index, row in enumerate (li):
                if row[index_column] == elmt:
                    return index

        tlinot_monster = [['ID', 'Type', 'ATK Power', 'DEF Power', 'HP']]
        for index, row in enumerate (li_monster):
            if index != 0 and findrow(row[0], 0, li_monster_shop) == None:
                tlinot_monster.append(row)

        tlinot_item = [['ID', 'Type']]
        for index, row in enumerate (li_item):
            if index != 0 and findrow(row[1], 0, li_item_shop) == None:
                new_row = [row[0], capital(row[1]) + ' Potion']
                tlinot_item.append(new_row)

        return tlinot_monster, tlinot_item
    
    def tableprint(tli): #tli matrix 3x3, minimal ada header, tiap row elmtnya lengkap
        def maxs(li):
            max_value = li[0]
            for elmt in li:
                if elmt > max_value:
                    max_value = elmt
            return max_value
        
        columnlength = [(maxs([len(str(row[column])) for row in tli])) for column in range (len(tli[0]))]
        for row in tli:
            for indeks, elmt in enumerate(row):
                if indeks != len(row)-1:
                    print(f"{elmt:<{columnlength[indeks]}} | ", end="")
                else:
                    print(f"{elmt:<{columnlength[indeks]}}")
        print()

    def tambahmonster(li_monster_shop, tlinot_monster):
        def isPInt(input):
            if len(input) == 0:
                return False
            else:
                for elmt in input:
                    if ord(elmt) not in range (48, 58):
                        return False
                return True
            
        def findrow(elmt, index_column, li): #cari index row, index_column start 0
            for index, row in enumerate (li):
                if row[index_column] == elmt:
                    return index
                
        idValid = False
        while not idValid:
            id = input("Masukkan id monster: ")
            if isPInt(id):
                if findrow(int(id), 0, tlinot_monster) == None:
                    print('Input tidak valid. Ulangi')
                else:
                    idValid = True
            else:
                print('Input tidak valid. Ulangi')

        stock = input("Masukkan stok awal: ")
        while not isPInt(stock):
            print('Input tidak valid. Ulangi')
            stock = input("Masukkan stok awal: ")

        price = input("Masukkan harga: ")
        while not isPInt(price):
            print('Input tidak valid. Ulangi')
            price = input("Masukkan harga: ")

        li_monster_shop.append([int(id), int(stock), int(price)])
        print(f"{tlinot_monster[findrow(int(id), 0, tlinot_monster)][1]} telah berhasil ditambahkan ke dalam shop!") #type selalu pada indeks kolom 1
        
        return li_monster_shop

    def tambahitem(li_item, li_item_shop, tlinot_item):
        def isPInt(input):
            if len(input) == 0:
                return False
            else:
                for elmt in input:
                    if ord(elmt) not in range (48, 58):
                        return False
                return True
            
        def findrow(elmt, index_column, li): #cari index row, index_column start 0
            for index, row in enumerate (li):
                if row[index_column] == elmt:
                    return index

        idValid = False
        while not idValid:
            id = input("Masukkan id potion: ")
            if isPInt(id):
                if findrow(int(id), 0, tlinot_item) == None:
                    print('Input tidak valid. Ulangi')
                else:
                    idValid = True
            else:
                print('Input tidak valid. Ulangi')

        stock = input("Masukkan stok awal: ")
        while not isPInt(stock):
            print('Input tidak valid. Ulangi')
            stock = input("Masukkan stok awal: ")

        price = input("Masukkan harga: ")
        while not isPInt(price):
            print('Input tidak valid. Ulangi')
            price = input("Masukkan harga: ")
        
        li_item_shop.append([li_item[findrow(int(id), 0, li_item)][1], int(stock), int(price)])
        print(f"{tlinot_item[findrow(int(id), 0, tlinot_item)][1]} telah berhasil ditambahkan ke dalam shop!")

        return li_item_shop

    def ubahmonster(li_monster_shop, tli_monster):
        def isPInt(input):
            if len(input) == 0:
                return False
            else:
                for elmt in input:
                    if ord(elmt) not in range (48, 58):
                        return False
                return True
            
        def findrow(elmt, index_column, li): #cari index row, index_column start 0
            for index, row in enumerate (li):
                if row[index_column] == elmt:
                    return index
                
        idValid = False
        while not idValid:
            id = input("Masukkan id monster: ")
            if isPInt(id):
                if findrow(int(id), 0, tli_monster) == None:
                    print('Input tidak valid. Ulangi')
                else:
                    idValid = True
            else:
                print('Input tidak valid. Ulangi')

        stock = input("Masukkan stok awal: ")
        while not isPInt(stock) and not len(stock) == 0:
            print('Input tidak valid. Ulangi')
            stock = input("Masukkan stok awal: ")

        price = input("Masukkan harga: ")
        while not isPInt(price) and not len(price) == 0:
            print('Input tidak valid. Ulangi')
            price = input("Masukkan harga: ")   

        isStockChange, isPriceChange = False, False
        if len(stock) != 0:
            li_monster_shop[findrow(int(id), 0, li_monster_shop)][1] = int(stock)
            isStockChange = True
        if len(price) != 0:
            li_monster_shop[findrow(int(id), 0, li_monster_shop)][2] = int(price)
            isPriceChange = True

        if isStockChange and isPriceChange:
            print(f"{tli_monster[findrow(int(id), 0, tli_monster)][1]} telah berhasil diubah dengan stok baru sejumlah {stock} dan dengan harga baru {price}!")
        elif isStockChange and not isPriceChange:
            print(f"{tli_monster[findrow(int(id), 0, tli_monster)][1]} telah berhasil diubah dengan stok baru sejumlah {stock}!")
        elif not isStockChange and isPriceChange:
            print(f"{tli_monster[findrow(int(id), 0, tli_monster)][1]} telah berhasil diubah dengan harga baru {price}!")
        else:
            print(f"{tli_monster[findrow(int(id), 0, tli_monster)][1]} sama sekali tidak diubah")
        
        return li_monster_shop

    def ubahitem(li_item, li_item_shop, tli_item):
        def isPInt(input):
            if len(input) == 0:
                return False
            else:
                for elmt in input:
                    if ord(elmt) not in range (48, 58):
                        return False
                return True
            
        def findrow(elmt, index_column, li): #cari index row, index_column start 0
            for index, row in enumerate (li):
                if row[index_column] == elmt:
                    return index
                
        idValid = False
        while not idValid:
            id = input("Masukkan id potion: ")
            if isPInt(id):
                if findrow(int(id), 0, tli_item) == None:
                    print('Input tidak valid. Ulangi')
                else:
                    idValid = True
            else:
                print('Input tidak valid. Ulangi')

        stock = input("Masukkan stok awal: ")
        while not isPInt(stock) and not len(stock) == 0:
            print('Input tidak valid. Ulangi')
            stock = input("Masukkan stok awal: ")

        price = input("Masukkan harga: ")
        while not isPInt(price) and not len(price) == 0:
            print('Input tidak valid. Ulangi')
            price = input("Masukkan harga: ")

        isStockChange, isPriceChange = False, False
        if len(stock) != 0:
            li_item_shop[findrow(li_item[findrow(int(id), 0, li_item)][1], 0, li_item_shop)][1] = int(stock)
            isStockChange = True
        if len(price) != 0:
            li_item_shop[findrow(li_item[findrow(int(id), 0, li_item)][1], 0, li_item_shop)][2] = int(price)
            isPriceChange = True

        if isStockChange and isPriceChange:
            print(f"{tli_item[findrow(int(id), 0, tli_item)][1]} telah berhasil diubah dengan stok baru sejumlah {stock} dan dengan harga baru {price}!")
        elif isStockChange and not isPriceChange:
            print(f"{tli_item[findrow(int(id), 0, tli_item)][1]} telah berhasil diubah dengan stok baru sejumlah {stock}!")
        elif not isStockChange and isPriceChange:
            print(f"{tli_item[findrow(int(id), 0, tli_item)][1]} telah berhasil diubah dengan harga baru {price}!")
        else:
            print(f"{tli_item[findrow(int(id), 0, tli_item)][1]} sama sekali tidak diubah")
        
        return li_item_shop

    def hapusmonster(li_monster_shop, tli_monster):
        def isPInt(input):
            if len(input) == 0:
                return False
            else:
                for elmt in input:
                    if ord(elmt) not in range (48, 58):
                        return False
                return True
            
        def isyorn(input):
            if len(input) == 0:
                return False
            else:
                if input.lower() in ['y', 'n']:
                    return True
                else:
                    return False
            
        def findrow(elmt, index_column, li): #cari index row, index_column start 0
            for index, row in enumerate (li):
                if row[index_column] == elmt:
                    return index

        def pops(li, index): #index start 0
            result = []
            for idx, elmt in enumerate (li):
                if idx != index:
                    result.append(elmt)
            return result
        
        idValid = False
        while not idValid:
            id = input("Masukkan id monster: ")
            if isPInt(id):
                if findrow(int(id), 0, tli_monster) == None:
                    print('Input tidak valid. Ulangi')
                else:
                    idValid = True
            else:
                print('Input tidak valid. Ulangi')

        choiceValid = False
        while not choiceValid:
            choice = input(f"Apakah anda yakin ingin menghapus {tli_monster[findrow(int(id), 0, tli_monster)][1]} dari shop (y/n)? ")
            if isyorn(choice):
                choiceValid = True
            else:
                print('Input tidak valid. Ulangi')

        if choice.lower() == "y":
            li_monster_shop = pops(li_monster_shop, findrow(int(id), 0, li_monster_shop))
            print(f"{tli_monster[findrow(int(id), 0, tli_monster)][1]} telah berhasil dihapus dari shop!")
        else:
            print(f"{tli_monster[findrow(int(id), 0, tli_monster)][1]} batal dihapus dari shop!")

        return li_monster_shop

    def hapusitem(li_item, li_item_shop, tli_item):
        def isPInt(input):
            if len(input) == 0:
                return False
            else:
                for elmt in input:
                    if ord(elmt) not in range (48, 58):
                        return False
                return True
            
        def isyorn(input):
            if len(input) == 0:
                return False
            else:
                if input.lower() in ['y', 'n']:
                    return True
                else:
                    return False
            
        def findrow(elmt, index_column, li): #cari index row, index_column start 0
            for index, row in enumerate (li):
                if row[index_column] == elmt:
                    return index

        def pops(li, index): #index start 0
            result = []
            for idx, elmt in enumerate (li):
                if idx != index:
                    result.append(elmt)
            return result
        
        idValid = False
        while not idValid:
            id = input("Masukkan id potion: ")
            if isPInt(id):
                if findrow(int(id), 0, tli_item) == None:
                    print('Input tidak valid. Ulangi')
                else:
                    idValid = True
            else:
                print('Input tidak valid. Ulangi')
        
        choiceValid = False
        while not choiceValid:
            choice = input(f"Apakah anda yakin ingin menghapus {tli_item[findrow(int(id), 0, tli_item)][1]} dari shop (y/n)? ")
            if isyorn(choice):
                choiceValid = True
            else:
                print('Input tidak valid. Ulangi')

        if choice.lower() == "y":
            li_item_shop = pops(li_item_shop, findrow(li_item[findrow(int(id), 0, li_item)][1], 0, li_item_shop))
            print(f"{tli_item[findrow(int(id), 0, tli_item)][1]} telah berhasil dihapus dari shop!")
        else:
            print(f"{tli_item[findrow(int(id), 0, tli_item)][1]} batal dihapus dari shop!")

        return li_item_shop

    def isActionValid(input):
        if len(input) == 0:
            return False
        else:
            if input.lower() in ['lihat', 'tambah', 'ubah', 'hapus', 'keluar']:
                return True
            else:
                return False

    def isMonsterOrPotion(input):
        if len(input) == 0:
            return False
        else:
            if input.lower() in ['monster', 'potion']:
                return True
            else:
                return False

    print("\nIrasshaimase! Selamat datang kembali, Mr. Monogram!\n")
    exit = False
    while not exit:
        action = input("\nPilih aksi (lihat/tambah/ubah/hapus/keluar): ")
        while not isActionValid(action):
            action = input("Input tidak valid. Ulangi\nPilih aksi (lihat/tambah/ubah/hapus/keluar): ")
            
        tli_monster, tli_item = load_tli(li_monster, li_item, li_monster_shop, li_item_shop)
        tlinot_monster, tlinot_item = load_tlinot(li_monster, li_item, li_monster_shop, li_item_shop)
        
        if action.lower() == "lihat":
            choice = input("Mau lihat apa? (monster/potion): ")
            while not isMonsterOrPotion(choice):
                choice = input("Input tidak valid. Ulangi\nMau lihat apa? (monster/potion): ")
            if choice.lower() == "monster":
                tableprint(tli_monster)
            else:
                tableprint(tli_item)

        elif action.lower() == "tambah":
            choice = input("Mau nambahin apa? (monster/potion): ")
            while not isMonsterOrPotion(choice):
                choice = input("Input tidak valid. Ulangi\nMau nambahin apa? (monster/potion): ")
            if choice.lower() == "monster":
                if len(tlinot_monster) == 1:
                    print("Tidak ada monster yang tersedia")
                else:
                    tableprint(tlinot_monster)
                    li_monster_shop = tambahmonster(li_monster_shop, tlinot_monster)
            else: 
                if len(tlinot_item) == 1:
                    print("Tidak ada potion yang tersedia")
                else:
                    tableprint(tlinot_item)
                    li_item_shop = tambahitem(li_item, li_item_shop, tlinot_item)
                
        elif action.lower() == "ubah":
            choice = input("Mau ubah apa? (monster/potion): ")
            while not isMonsterOrPotion(choice):
                choice = input("Input tidak valid. Ulangi\nMau ubah apa? (monster/potion): ")
            if choice.lower() == "monster":
                if len(tli_monster) == 1:
                    print("Tidak ada monster yang tersedia")
                else:
                    tableprint(tli_monster)
                    li_monster_shop = ubahmonster(li_monster_shop, tli_monster)
            else:
                if len(tli_item) == 1:
                    print("Tidak ada item yang tersedia")
                else:
                    tableprint(tli_item)
                    li_item_shop = ubahitem(li_item, li_item_shop, tli_item)
            
        elif action.lower() == "hapus":
            choice = input("Mau hapus apa? (monster/potion): ")
            while not isMonsterOrPotion(choice):
                choice = input("Input tidak valid. Ulangi\nMau hapus apa? (monster/potion): ")
            if choice.lower() == "monster":
                if len(tli_monster) == 1:
                    print("Tidak ada monster yang tersedia")
                else:
                    tableprint(tli_monster)
                    li_monster_shop = hapusmonster(li_monster_shop, tli_monster)
            else:
                if len(tli_item) == 1:
                    print("Tidak ada item yang tersedia")
                else:
                    tableprint(tli_item)
                    li_item_shop = hapusitem(li_item, li_item_shop, tli_item)
        else:
            print("Dadah Mr. Yanto, sampai jumpa lagi!\n")
            exit = True
    return li_monster, li_monster_shop, li_item_shop

# li_monster = [['id', 'type', 'atk_power', 'def_power', 'hp'], [1, 'Pikachow', 11, 111, 1111], [2, 'Bulbu', 22, 222, 2222], [3, 'Zeze', 33, 333, 3333], [4, 'Iqbal', 44, 444, 4444]]
# li_monster_shop = [['monster_id', 'stock', 'price'], [1, 10, 100], [2, 20, 200], [3, 30, 300]]
# li_item_shop = [["type", 'stock', 'price'], ['strength', 10, 50], ['resilience', 5, 30]]
# li_item = [['potion_id', 'type'], [1, 'strength'], [2, 'resilience'], [3, 'healing']]

# li_monster, li_monster_shop, li_item_shop = shop_management(li_monster, li_item, li_monster_shop, li_item_shop)
# print(li_monster, '\n', li_item, '\n', li_monster_shop, '\n', li_item_shop)
