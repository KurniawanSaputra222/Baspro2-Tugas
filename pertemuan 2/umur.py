umur = int(input("Masukkan Usia Anda: "))

if umur <= 5:
    print("adalah balita")
elif umur > 5 and umur <= 13:
    print("termasuk Anak-anak")
elif umur > 13 and umur <= 25:
    print("termasuk remaja")
elif umur > 25 and umur <= 35:
    print("termasuk Dewasa")
elif umur > 35 and umur <= 55:
    print("termasuk Orang tua")
else:
    print("termasuk lansia")