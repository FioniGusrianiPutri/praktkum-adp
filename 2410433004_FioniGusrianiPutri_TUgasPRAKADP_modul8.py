def pisah_judul_isi (baris) :
    judul = ""
    isi = ""
    i = 0
    while i < len(baris) - 1 :
        if baris[i] == "|" and baris[i+1] == "|" :
            isi = baris[i+2:]
            break
        judul += baris[i]
        i += 1
    hasil = ""
    for a in isi :
        if a != "\n" :
            hasil += a
    isi = hasil
    return judul, isi


def baca_catatan() :
    catatan = {}
    file = open("catatan.txt", "r")
    for baris in file :
        if "||" in baris :
            judul, isi = pisah_judul_isi(baris)
            catatan[judul] = isi
    file.close()
    return catatan

def simpan_catatan(judul, isi) :
    file = open("catatan.txt", "a")
    file.write(judul + "||" + isi + "\n")
    file.close()

def main() :
    while True :
        print("menu utama")
        print("1. lihat catatan")
        print("2. buat catatan baru")
        print("3. exit")
        pilih = input("pilih : ")
        
        if pilih == "1" :
            catatan = baca_catatan()
            if len(catatan) == 0 :
                print("belum ada catatan")
            else :
                print("\njudul catatan yang tersedia : ")
                for judul in catatan :
                    print("-" + judul)
                cari = input("masukkan judul : ")
                if cari in  catatan :
                    print("isi :", catatan[cari])
                else :
                    print("data tidak ditemukan")

        elif pilih == 2 :
            judul = input("masukkan judul catatan : ")
            isi = input("masukkan isi catatn: ")
            simpan_catatan(judul, isi)
            print("catatn berhasil di simpan")

        elif pilih == 3 :
            print("keluar dari program")
            break

        else :
            print("pilihan tidak valid")

main()
        
