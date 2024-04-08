import csv
# Izdvoji 10 najpop pjesmama ciji naziv pocinje sa Velikim slovom sortiranje po Energy u opadajuci

with open('pjesme.csv') as pjesme:
    sadrzaj = csv.reader(pjesme)
    header = next(sadrzaj)
    lista = []
    for red in sadrzaj:
        lista.append(red)
    lista_imena=[]
    for elem in lista:
        if elem[1][0].isupper():
            lista_imena.append(elem)
    lista_imena.sort(key= lambda x:x[4])
    f = open("zadatak3.csv",'w', newline='')
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(lista_imena[:10])


