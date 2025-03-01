x = int(input("A = "))
if x %2  == 0:
    print(f"Inputan A yang bernilai {x} = Genap")
else:
    print(f"Inputan A yang bernilai {x} = Ganjil")

y = int(input("B = "))
if y %2  == 0:
    print(f"Inputan B yang bernilai {y} = Genap")
else:
    print(f"Inputan B yang bernilai {y} = Ganjil")
z = (x + y)
print(type(z))
print(f" A + B = {z}")
if z %2  == 0:
    print(f"Hasil dari {x} + {y} = {z} = Genap")
else:
    print(f"Hasil dari {x} + {y} = {z} = Ganjil")
z = (x + y)