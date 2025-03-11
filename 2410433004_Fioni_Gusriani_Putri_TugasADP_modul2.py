nama_barang = ["galon", "sapu", "wajan", "sutil", "cermin", "rak sepatu"]
harga_satuan = ["78000, 60000, 50000, 60000, 80000, 50.000"]

#tampilkan daftar barang
print("daftar barang yang di jual")
print("1. galon - Rp. 78.000")
print("2. sapu - Rp. 60.000")
print("3. wajan - Rp. 50.000")
print("4. sutil - Rp. 20.000")
print("5. cermin - Rp. 60.000")
print("6. rak sepatu - Rp. 50.000")

#pilih barang
pilih = int(input("masukkan nomor barang : "))
jumlah = int(input("masukkan jumlah barang : "))

if pilih == 1 :
    nama_barang = "galon"
    harga_satuan = 78000
elif pilih == 2 :
    nama_barang = "sapu"
    harga_satuan = 60000
elif pilih == 3 :
    nama_barang = "wajan"
    harga_barang = 50000
elif pilih == 4 :
    nama_barang = "sutil"
    harga_barang = 640000
elif pilih == 5 :
    nama_barang = "cermin"
    harga_barang = 80000
elif pilih == 6 :
    nama_barang = "rak sepatu"
    harga_satuan = 50000

#hitung harga sebelum diskon
total_harga = harga_satuan * jumlah

#diskon
if total_harga >= 1500000 :
    diskon = total_harga * 0.15
elif total_harga >= 1000000 :
    diskon = total_harga * 0.10
else :
    diskon = 0 #tidak da diskon

#total harga yang di hasilkan
total_bayar= total_harga - diskon

#buat struk pembeliannya
print("=====STRUK PEMBELIAN=====")
print("=====TOKO FIFIFA PERABOT=====")
print("nama barang  :", nama_barang)
print("kuantitas    :", jumlah)
print("harga satuan : Rp", harga_satuan)
print("total harga  : Rp", total_harga)
print("ptongan harga: Rp", diskon)
print("total bayar  : Rp", total_bayar)
print("==========================")
print("=====terima kasih telah berbelanja=====")
