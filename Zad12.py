sb = int(input("Stevanovi bodovi: "))
sv = int(input("Stevanovo vrijeme u minutima: "))
dv = int(input("Dejanovo vijeme u minutima: "))
db = int(input("Dejanovi bodovi: "))
s = sv * sb
d = dv * db
s
if s > d:
    print(f"Stefan je dobio sa rezultatom {s}, njegovi bodovi su {sb}, a vrijeme {sv}")
else:   
    print(f"Dejan je dobio sa rezultatom {d}, njegovi bodovi su {db}, a vrijeme {dv}")