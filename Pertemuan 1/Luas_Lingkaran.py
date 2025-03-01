from fractions import Fraction
r = int(input("Silahkan Masukkan Jari-jari Lingkaran = "))
if r % 7 == 0:
    phi = Fraction(22,7)
else:
    phi = 3.14

l = phi * r ** 2

print(f"Rumus Luas Lingkaran = phi x r(jari-jari)^2")
print(f"Hasil dari Luas lingkaran {phi} x {r}^2 = {l}")