def update_list(a,x):    
    for i in range(len(a)):
        if a[i]%2 ==0:
            a[i] += x
    print(a)
lista = [1,4,2,5,8]
t= 3
update_list(lista, t)

    