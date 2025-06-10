import os
import time
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def gambar_kue(api_char='*'):
    kue = []
    kue.append(colored("     " + api_char + "     ", "yellow"))
    kue.append(colored("     |     ", "blue"))

    # Lapisan-lapisan kue
    lapisan = [
        ("#"*11, "red"),
        ("="*13, "magenta"),
        ("~"*15, "cyan")
    ]

    for bentuk, warna in lapisan:
        spasi = " " * ((15 - len(bentuk)) // 2)
        baris = spasi + bentuk + spasi
        kue.append(colored(baris, warna))

    return kue

def simpan_ke_file(kue, nama_file="kue.txt"):
    with open(nama_file, "w") as f:
        for baris in kue:
            clean_line = baris.replace('\x1b', '').split('m')[-1]
            f.write(clean_line + "\n")

def animasi_lilin(durasi_detik=5):
    simbol_api = ['', 'o', '+', '^', '']
    start = time.time()

    while time.time() - start < durasi_detik:
        for s in simbol_api:
            clear()
            print(colored("\n  Selamat Ulang Tahun!\n", "green", attrs=["bold"]))
            kue = gambar_kue(api_char=s)
            for baris in kue:
                print(baris)
            time.sleep(0.3)

def main():
    clear()
    print(colored("Membuat kue ulang tahun...\n", "cyan"))

    kue = gambar_kue()
    for baris in kue:
        print(baris)

    simpan_ke_file(kue)
    print("\nKue disimpan ke file 'kue.txt'.")

    input("\nTekan ENTER untuk menyalakan lilin...")
    animasi_lilin(6)
    print(colored("\nSemoga harimu menyenangkan! :)", "yellow"))

main()
