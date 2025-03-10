nama = input("masukkan Nama: ")
nik = input("masukkan NIK: ")
status = input("masukkan Status (pegawai Tetap/Honor): ")
golongan = input("masukkan Golongan (A/B/C): ")

gaji = 0
bonus = 0

if status.lower() == "pegawai tetap":
    gaji = 1000000
    if golongan.lower() == "a":
        bonus = 200000
    elif golongan.lower() == "b":
        bonus = 400000
    elif golongan.lower() == "c":
        bonus = 550000
    else:
        print("Golongan tidak valid!")
elif status.lower() == "honor":
    gaji = 750000
    if golongan.lower() == "a":
        bonus = 150000
    elif golongan.lower() == "b":
        bonus = 275000
    elif golongan.lower() == "c":
        bonus = 480000
    else:
        print("Golongan tidak valid!")
else:
    print("Status tidak valid!")

totalgaji = gaji + bonus

print("\n=== Rincian Gaji ===")
print("Nama:", nama)
print("NIK:", nik)
print("Status:", status)
print("Golongan:", golongan)
print("Gaji Pokok: Rp", gaji)
print("Bonus: Rp", bonus)
print("Gaji Total: Rp", totalgaji)