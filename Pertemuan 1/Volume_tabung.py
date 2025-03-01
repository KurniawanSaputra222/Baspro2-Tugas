from fractions import Fraction
r = int(input("Silahkan Masukkan Jari-jari Tabung: "))
if r%7 == 0:
    phi = Fraction(22,7)
else:
    phi = 3.14
t = int(input("Silahkan Masukkan Tinggi Tabung: "))
v = phi*r**2*t
print(f"Rumus Volume tabung = phi x r^2 x t ")
print(f"Hasil dari Volume tabung dengan {phi} x {r}^2 x {t} = {v}")