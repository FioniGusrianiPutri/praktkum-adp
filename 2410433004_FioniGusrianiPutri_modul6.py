jumlah_kasus = int(input("masukkan jumlah system SPL : "))
semua_kasus = []
semua_konstanta = []

for i in range(jumlah_kasus) :
    print("SPL ke ", i+1)
    n = int(input("jumlah persamaan : "))
    m = int(input("jumlah variabel : "))
    if n not in [2, 3] or m not in [2, 3] :
        print("input tidak valid, hanya terdapat 2 atau 3")
        continue

    A = []
    B = []

    for j in range (n) :
        row = []
        for k in range (m) :
            row.append(float(input(f"koefisien x{k+1} di persamaan {k+1} : ")))
        A.append(row)
        B.append(float(input(f"koefisien di persamaan {i+1} : ")))
    semua_kasus.append(A)
    semua_konstanta.append(B)

print("hasil")
for l in range(len(semua_kasus)) :
    A = semua_kasus[l]
    B = semua_konstanta[l]
    print(f"SPL ke {l+1}: ")

    n = len(A)
    m = len(A[0])

    if n != m :
        if n > m :
            print("tidak ada solusi unik")
        else :
            print("tidak hingga solusi")
        continue

    if m == 2 :
        det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else :
        det_A = (
            A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1]) -
            A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) +
            A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
        )

    if det_A == 0 :
        print("tidak ada solusi unik")
        continue

    solusi = []
    for j in range(m) :
        baris_baru = []
        for k in range(n) :
            baris = A[k][:]
            baris[i] = B[j]
            baris_baru.append(baris)
        
        if m == 2 :
            det_Aj = baris_baru[0][0]*baris_baru[1][1] - baris_baru[1][0]
        else :
            det_Aj = (
                baris_baru[0][0]*(baris_baru[1][1]*baris_baru[2][2] - baris_baru[1][2]*baris_baru[2][1]) -
                baris_baru[0][1]*(baris_baru[1][0]*baris_baru[2][2] - baris_baru[1][2]*baris_baru[2][0]) +
                baris_baru[0][2]*(baris_baru[1][0]*baris_baru[2][1] - baris_baru[1][1]*baris_baru[2][0])
            )
        solusi.append(det_A / det_A)

    for j in range(m) :
        print(f"x{i+1} = {solusi[j]}")