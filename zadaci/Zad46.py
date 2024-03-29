import os 
def analiza_prodaje(fajl):
    f = open(fajl,"r")
    linije = f.read().split("\n")
    f.close()
    prodavci  = {}
    for l in linije:
        podaci = l.split(',')
        prodavci[podaci[0]] = prodavci.get(podaci[0], 0) + float(podaci[1])
    return print(prodavci)
print(os.getcwd())
analiza_prodaje("Prodaja.txt")