def dodaj_proizvode(n):
    lista_proizvoda=[]
    for i in range(n):
        naziv=input("Unesi naziv: ")
        opis= input ("Unesi opis: ")
        cijena=float(input("Unesi cijenu: "))
        print(f"unesen artikal br: {i+1}")
        lista_proizvoda.append({"naziv":naziv,"opis":opis,"cijena":cijena,"broj_artikala":i+1})
    return lista_proizvoda

def kupovina(proizvodi, naziv, raspolozivi_novac):
    for prozivod in proizvodi:
        if prozivod["naziv"] == naziv:
            maxim = int(raspolozivi_novac / prozivod["cijena"])
            if maxim > prozivod["broj_artikala"]:
                print(prozivod["broj_artikala"])
            else:
                print(maxim)
    
proizvodi = dodaj_proizvode(2)
kupovina(proizvodi, "Iphon", 600)


