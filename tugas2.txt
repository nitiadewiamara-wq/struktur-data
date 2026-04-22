# Validasi nama
nama_benar = "niti"  # ganti dengan nama pendek yang diinginkan

while True:
    nama = input("Masukan nama anda (nama pendek anda): ")
    
    if nama.lower() == nama_benar:
        print("Nama benar, lanjut ke program...\n")
        break
    else:
        print("Silahkan coba lagi!\n")

# Input angka
angka = int(input("Masukkan angka: "))

# Menampilkan tabel perkalian 1 - 10
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")
