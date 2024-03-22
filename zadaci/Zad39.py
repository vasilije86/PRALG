def najmanji_grad(file, drzava):   
    naj = 9999999999999999
    grad = ""
    f = open(file, "r")
    linija  = f.read().split("\n")
    f.close()
    for red in linija:
        drzava1 = red.split(",")
        if drzava1[0]==drzava:
            populacija=int(drzava1[2])
            if populacija < naj:
                naj = populacija
                grad = drzava1[1]
    return grad
       
print(najmanji_grad("C:/Users/vasil/Documents/Fax/4.semestar/PRALG/PRALG/zadaci/Countries.txt", "Poljska"))