def dodaj_proizvode(n):
    lista_proizvoda=[]
    for i in range(n):
        naziv=input("Unesi naziv: ")
        opis= input ("Unesi opis: ")
        cijena=float(input("Unesi cijenu: "))
        print(f"unesen artikal br: {i+1}")
        lista_proizvoda.append({"naziv":naziv,"opis":opis,"cijena":cijena,"broj_artikala":i+1})
    return lista_proizvoda

proizvodi=dodaj_proizvode(2)

def search(proizvodi, search_term):
    lista = []
    for proizvod in proizvodi:        
        if proizvod.get("naziv") == search_term: 
            lista.append(proizvod)
    print(lista)

search(proizvodi,"Telefon")

