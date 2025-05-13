no_pelanggan    = [ ]
nama_pelanggan  = [ ]
total_belanja   = [ ]

for i in range(4) :
    print("MENU")
    print("1. Tambah Data")
    print("2. Hapus data")
    print("3. Tambilkan Data")
    print("4. Keluar")
    pilih = input("pilih nemu (1-4): ")

    if pilih == "1" :
        ulang = "Y"
        while ulang == "Y" or ulang == "y" :
            no      = input("masukkan no. pelanggan         : ")
            nama    = input("masukkan nama pelanggan        : ")
            total   = float(input("masukkan total belanja pelanggan  : "))

            no_pelanggan.append(no)
            nama_pelanggan.append(nama)
            total_belanja.append(total)

            ulang = input("tambahkan data lagi? (yes/no) : ")
    
    elif pilih == "2" :
        hapus = input("masukkan no pelanggan yang dihapus : ")
        ditemukan = False
        for j in range(len(no_pelanggan)) :
            if hapus in no_pelanggan :
                del no_pelanggan[j]
                del nama_pelanggan[j]
                del total_belanja[j]
                ditemukan = True
                print("data berhasil dihapus")
                break 
        if not ditemukan :
            print("data tidak dapat ditemukan")

    elif pilih == "3" :
        print("Data Pelanggan")
        if len(no_pelanggan) == 1 :
            print("belum ada data")
        else :
            for j in range(len(no_pelanggan)) : 
                print(f"{j+1}. {no_pelanggan[j]} - {nama_pelanggan[j]} - Rp{total_belanja[j]:,.2f}")
    
    elif pilih == "4" :
        print("terima kasih, program selesai")
        break
    
    else :
        print("pilihan tidak valid, silahkan coba lagi")