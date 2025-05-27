def hitung_tagihan (kwh, gol) :
    tarif_awal = [1500, 2500, 4000, 5000]
    tarif_berikutnya = [2000, 3000, 5000, 7000]

    if gol == 0 :
        gol = 3
    
    x = gol - 1

    if kwh <= 100 :
        return kwh * tarif_awal[x]
    else :
        return 100 * tarif_awal[x] + (kwh - 100) * tarif_berikutnya[x]
    
kwh = int(input("masukkan pemakaian kwh : "))
golongan = input("masukkan golongan, kosong = 3 : ")

if golongan == "" :
    gol = 0
else :
    gol = int(golongan)

tagihan = hitung_tagihan(kwh, gol)
print("total tagihan : Rp.", tagihan)