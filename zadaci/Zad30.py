def presjek(lista1, lista2):
    lista3 = list()
    for i in lista1:
        for j in lista2:
            if i == j:
                lista3.append(i)
    print(set(lista3))
    
lista1 = [1,2,3,6,6,7]
lista2 = [4,5,6,7,6,7,8]

presjek(lista1, lista2)
