s = input("Unesite broj: ")
if s.startswith("0b"):
    print('korisnik je unio binarni')
elif s.startswith("0x"):
    print('korisnik je unio hexadecimalni')
elif s.startswith("0o"):
    print('korisnik je unio octalni')
else:
    print("korisnik je unio dekadni")
