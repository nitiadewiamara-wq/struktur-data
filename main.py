
# Input nama
nama = input("Masukkan nama anda: ")

# Cek nama (misal tidak boleh kosong)
if nama != "":
    print("Selamat datang", nama)
else:
    print("Program selesai")

# Input umur
umur = int(input("Masukkan umur anda: "))

# Percabangan umur
if umur >= 18:
    print("anda cukup umur")
elif umur < 18 and umur > 0:
    print("anda belum cukup umur")
elif umur <= 0:
    print("anda belum lahir")

if umur > 60:
    print("banyakin ibadah, bentar lagi mati")

print("Program selesai")