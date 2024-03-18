def second_max(a):
    a = list(set(a))
    a.sort(reverse = True)
    print(a[1])
lista = [1,2,3,1]
second_max(lista)
