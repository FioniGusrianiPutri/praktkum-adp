n = int(input("masukkan jumlah partisi (n): "))

if n <= 0 :  
    print("masukkan jumlah partisi lebih besar dari 0")
elif n == 1 :
    print("hasil dengan 1 partisi akan kurang akurat, coba yang lebih besar")
else :
    # di ketahui batas bawah dan batas bawah 
    a = 1
    b = 3
    dx = (b - a) / n # rumus delta x atau panjang partisi
    i = 0
    luas = 0
    for i in range (n) :
        x = a + ( i + 1 ) * dx
        fungsi = x**2 + 2*x
        luas  += fungsi * dx
    print("luas daerah dari fungsi x**2 + 2*x dengan batas daerah x = 1 dan x = 3 dan jumlah pastisi n ", n, "adalah", luas, "(estimasi luas daerah)")