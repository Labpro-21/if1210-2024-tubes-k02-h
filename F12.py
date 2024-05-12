#fungsi illegal: pop, slicing

def shop_management(li_monster, li_monster_shop, li_item_shop): #yang bisa masuk pasti rolenya admin
    def loadshop(li_monster, li_monster_shop, li_item_shop):
        def capital(string):
            lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for index, elmt in enumerate(lower):
                if string[0] == elmt:
                    capital_string = upper[index]
            for i in range (1, len(string)):
                capital_string += string[i]
            return(capital_string)

        def popm(li, index): #index start 0, always defined
            result = []
            for i in range (len(li)):
                if i != index:
                    result.append(li[i])
            return result

        tli_monster = [['ID', 'Type', 'ATK Power', 'DEF Power', 'HP', 'Stock', 'Price']] #header
        for row1 in li_monster_shop:
            for row2 in li_monster:
                if row1[0] == row2[0]:
                    row1 = popm(row1, 0) #id selalu index col 1
                    row = row2 + row1
                    tli_monster.append(row)

        tli_potion = [['ID', 'Type', 'Stok', 'Harga']] #header
        for index, row in enumerate (li_item_shop):
            #row[0] = capital(row[0]) + ' Potion' #row type ada di col indeks = 0
            #row[0] = row[0] + ' Potion' #row type ada di col indeks = 0
            row = [index] + row
            tli_potion.append(row)
        tli_potion = popm(tli_potion, 1) #row nama kolom list_item_shop selalu di indeks = 0
            
        return tli_monster, tli_potion
    
    def tableprint(li): #li matrix 3x3 minimal ada header, tiap row elmtnya lengkap
        columnlength = [(max([len(str(row[column])) for row in li])) for column in range (len(li[0]))]
        for row in li:
            for indeks, elmt in enumerate(row):
                print(f"{elmt:<{columnlength[indeks]}} | ", end="")
            print()

    def notin(li_monster, li_monster_shop, li_item_shop):
        def popm(li, index): #index start 0, always defined
            result = []
            for i in range (len(li)):
                if i != index:
                    result.append(li[i])
            return result
        
        def capital(string):
            lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for index, elmt in enumerate(lower):
                if string[0] == elmt:
                    capital_string = upper[index]
            for i in range (1, len(string)):
                capital_string += string[i]
            return(capital_string)

        notin_monster = [['ID', 'Type', 'ATK Power', 'DEF Power', 'HP']]
        for row1 in li_monster:
            isExist = False
            for row2 in li_monster_shop:
                if row1[0] == row2[0]:
                    isExist = True
            if not isExist:
                notin_monster.append(row1)
        notin_monster = popm(notin_monster, 1) #index col selalu 1

        li_item = ['strength', 'resilience', 'healing']
        notin_potion = [['ID', 'Type']]
        id_cout = 1
        for elmt in li_item:
            isExist = False
            for row in li_item_shop:
                if elmt == row[0]:
                    isExist = True
            if not isExist:
                #elmt = capital(elmt) + ' Potion'
                #elmt = elmt + ' Potion'
                notin_potion.append([id_cout, elmt])
                id_cout += 1

        return notin_monster, notin_potion
    
    def tambahmonster(li_monster, li_monster_shop):
        id = int(input("Masukkan id monster: ")) #validasi none, int, in notin_monster
        stock = int(input("Masukkan stok awal: ")) #validasi int >0, none
        price = int(input("Masukkan harga: ")) #validasi int >0, none
        li_monster_shop.append([id, stock, price])
        for row in li_monster:
            if row[0] == id:
                print(f"{row[1]} telah berhasil ditambahkan ke dalam shop!") #type selalu pada indeks kolom 1
        
        return li_monster_shop

    def tambahpotion(notin_potion, li_item_shop):
        id = int(input("Masukkan id potion: ")) #validasi none, int, in notin_monster
        stock = int(input("Masukkan stok awal: ")) #validasi int >0, none
        price = int(input("Masukkan harga: ")) #validasi int >0, none
        
        for row in notin_potion:
            if row[0] == id:
                row[1] = row[1].lower()
                row[1] = row[1].rstrip(" potion")
                li_item_shop.append([row[1], stock, price])

        return li_item_shop

    def ubahmonster(li_monster_shop, li_monster):
        id = int(input(f"Masukkan id monster: ")) #validasi none, int, inlistshop
        stock = input(f"Masukkan stok baru: ") #validasi int
        price = input(f"Masukkan harga baru: ") #validasi int

        for index_row, row in enumerate(li_monster_shop):
            if row[0] == id:
                break    

        isStockChange, isPriceChange = False, False
        if len(stock) != 0:
            li_monster_shop[index_row][1] = int(stock)
            isStockChange = True
        if len(price) != 0:
            li_monster_shop[index_row][2] = int(price)
            isPriceChange = True

        for i in range (len(li_monster)):
            if li_monster[i][0] == id:
                break

        if isStockChange and isPriceChange:
            print(f"{li_monster[i][1]} telah berhasil diubah dengan stok baru sejumlah {stock} dan dengan harga baru {price}!")
        elif isStockChange and not isPriceChange:
            print(f"{li_monster[i][1]} telah berhasil diubah dengan stok baru sejumlah {stock}!")
        elif not isStockChange and isPriceChange:
            print(f"{li_monster[i][1]} telah berhasil diubah dengan harga baru {price}!")
        else:
            print(f"{li_monster[i][1]} sama sekali tidak diubah")
        
        return li_monster_shop

    def ubahpotion(li_item_shop, tli_potion):
        id = int(input(f"Masukkan id potion: ")) #validasi none, int, inlistshop
        stock = input(f"Masukkan stok baru: ") #validasi int
        price = input(f"Masukkan harga baru: ") #validasi int

        for row in tli_potion:
            if row[0] == id:
                break
        change_type = row[1].lower() 
        change_type = change_type.rstrip(" potion") #nama potionnya

        for row2 in li_item_shop:
            if change_type == row2[0]:
                isStockChange, isPriceChange = False, False
                if len(stock) != 0:
                    row2[1] = int(stock)
                    isStockChange = True
                if len(price) != 0:
                    row2[2] = int(price)
                    isPriceChange = True

        if isStockChange and isPriceChange:
            print(f"{row[1]} telah berhasil diubah dengan stok baru sejumlah {stock} dan dengan harga baru {price}!")
        elif isStockChange and not isPriceChange:
            print(f"{row[1]} telah berhasil diubah dengan stok baru sejumlah {stock}!")
        elif not isStockChange and isPriceChange:
            print(f"{row[1]} telah berhasil diubah dengan harga baru {price}!")
        else:
            print(f"{row[1]} sama sekali tidak diubah")
        
        return li_item_shop

    def hapusmonster(li_monster_shop, li_monster):
        def popm(li, index): #index start 0, always defined
            result = []
            for i in range (len(li)):
                if i != index:
                    result.append(li[i])
            return result
        
        id = int(input(f"Masukkan id monster: "))
        for row in li_monster:
            if row[0] == id:
                break

        choice = str(input(f"Apakah anda yakin ingin menghapus {row[1]} dari shop (y/n)? ")).lower() #validate except x/y
        if choice == "y":
            for indeks, row2 in enumerate(li_monster_shop):
                if row2[0] == id:
                    li_monster_shop = popm(li_monster_shop, indeks)
            print(f"{row[1]} telah berhasil dihapus dari shop!")
        else:
            print(f"{row[1]} batal dihapus dari shop!")

        return li_monster_shop

    def hapuspotion(li_item_shop, tli_potion):
        def popm(li, index): #index start 0, always defined
            result = []
            for i in range (len(li)):
                if i != index:
                    result.append(li[i])
            return result
        
        id = int(input(f"Masukkan id potion: "))
        for row in tli_potion:
            if row[0] == id:
                break

        choice = str(input(f"Apakah anda yakin ingin menghapus {row[1]} dari shop (y/n)? ")).lower() #validate except x/y
        if choice == "y":
            remove_type = row[1].lower()
            remove_type = remove_type.rstrip(' potion')
            for indeks, row2 in enumerate(li_item_shop):
                if row2[0] == remove_type:
                    li_item_shop = popm(li_item_shop, indeks)
            print(f"{row[1]} telah berhasil dihapus dari shop!")
        else:
            print(f"{row[1]} batal dihapus dari shop!")

        return li_item_shop

    print("\nIrasshaimase! Selamat datang kembali, Mr. Monogram!\n")
    while True:
        action = str(input("Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")).lower()
        if action == "lihat":
            tli_monster, tli_potion = loadshop(li_monster, li_monster_shop, li_item_shop)
            choice = str(input("Mau lihat apa? (monster/potion): ")).lower()
            if choice == "monster":
                tableprint(tli_monster)
            else:
                tableprint(tli_potion)

        elif action == "tambah":
            notin_monster, notin_potion = notin(li_monster, li_monster_shop, li_item_shop)
            choice = str(input("Mau nambahin apa? (monster/potion): ")).lower()
            if choice == "monster":
                tableprint(notin_monster)
                li_monster_shop = tambahmonster(li_monster, li_monster_shop)
            else: 
                tableprint(notin_potion)
                li_monster_shop = tambahpotion(notin_potion, li_item_shop)
                
        elif action == "ubah":
            tli_monster, tli_potion = loadshop(li_monster, li_monster_shop, li_item_shop)
            choice = str(input("Mau ubah apa? (monster/potion): ")).lower()
            if choice == "monster":
                tableprint(tli_monster)
                li_monster_shop = ubahmonster(li_monster_shop, li_monster)
            else: 
                tableprint(tli_potion)
                li_item_shop = ubahpotion(li_item_shop, tli_potion)
            
        elif action == "hapus":
            tli_monster, tli_potion = loadshop(li_monster, li_monster_shop, li_item_shop)
            choice = str(input("Mau hapus apa? (monster/potion): ")).lower()
            if choice == "monster":
                tableprint(tli_monster)
                li_monster_shop = hapusmonster(li_monster_shop, li_monster)
            else: 
                tableprint(tli_potion)
                li_item_shop = hapuspotion(li_item_shop, tli_potion)
            
        else:
            print("Dadah Mr. Yanto, sampai jumpa lagi!\n")
            break
    return li_monster, li_monster_shop, li_item_shop

li_monster = [['id', 'type', 'atk_power', 'def_power', 'hp'], [1, 'Pikachow', 11, 111, 1111], [2, 'Bulbu', 22, 222, 2222], [3, 'Zeze', 33, 333, 3333], [4, 'Iqbal', 44, 444, 4444]]
li_monster_shop = [['monster_id', 'stock', 'price'], [1, 10, 100], [2, 20, 200], [3, 30, 300]]
li_item_shop = [["type", 'stock', 'price'], ['strength', 10, 50], ['resilience', 5, 30]]

li_monster, li_monster_shop, li_item_shop = shop_management(li_monster, li_monster_shop, li_item_shop)