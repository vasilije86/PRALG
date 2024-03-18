def city(file, grad):   
    naj = 0
    naselje = ""
    f = open(file, "r")
    linija  = f.read().split("\n")
    f.close()
    for red in linija:
        grad1 = red.split(",")
        if grad1[0]==grad:
            populacija=int(grad1[2])
            if populacija> naj:
                naj = populacija
                naselje = grad1[1]
    return naselje
       
print(city("Cities.txt", "Podgorica"))

