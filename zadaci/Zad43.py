def segment(start, end):
    lista = []
    suma = 0
    for i in range(start, end + 1):
        if i % 3 ==0 and i % 6 != 0:
            lista.append(i ** 2)
            suma += i ** 2
            print(i)
    lista.append(suma)
    return lista

print(segment(3, 10))

    