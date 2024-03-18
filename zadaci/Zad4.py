broj = 3568
cif1 = (broj//100)%10
cif2 = broj %10
sifra = (cif1* cif2)** 0.5
print(f'Sifra ulaza je {sifra}')