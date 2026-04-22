
# Nama yang benar (ganti sesuai keinginan)
nama_benar = "dwi"

# Input nama
while True:
    nama = input("Masukkan nama anda (nama pendek): ")
    if nama.lower() == nama_benar:
        print("Nama benar! Lanjut ke program...\n")
        break
    else:
        print("Silahkan coba lagi!\n")

# Input angka
angka = int(input("Masukkan angka: "))

# Tabel perkalian 1 - 10
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")
