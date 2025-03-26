# input jumlah pendaftar
n = int(input("masukkan jumlah pendaftar : "))
# input nama, mata kuliah, penilaian nilai wawancara, penilaian test tulis, penilaiam mengajar di dalam perulangan
for i in range (1, n+1) :
    print(f"data pendaftar ke-{i} : ")
    nama = input("nama : ")
    mata_kuliah = input("mata kuliah yang diminati : ")
    
    total_nilai = 0
    # perulangan bersarang
    for j in range (3) :
        while True :
            if j == 0 :
                nilai = float(input("nilai wawancara: "))
            elif j == 1 :
                nilai = float(input("nilai test tulis: "))
            else :
                nilai = float(input("nilai mengajar: "))
            
            if 1 <= nilai <= 100 :
                total_nilai += nilai
                break
            else :
                print("nilai antara 1-100")
    # didalam perulangan jika rata rata nya
    rata_rata = total_nilai / 3
    # menentukan predikat
    if rata_rata > 80 :
        predikat = "lulus"
    else :
        predikat = "tidak lulus"
    print(f"{predikat}", end=" ")
    print( )

