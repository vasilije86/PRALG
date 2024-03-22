def najmanji_grad(file, drzava):   
    population = 0
    grad = ""
    f = open(file, "r")
    linija  = f.read().split("\n")
    f.close()
    for red in linija:
        drzava1 = red.split(",")
        if drzava1[0]==drzava:
            population += int(drzava1[2])
    return print(population)
       
najmanji_grad("C:/Users/vasil/Documents/Fax/4.semestar/PRALG/PRALG/zadaci/Countries.txt", "Poljska")