def unesi_ocjene(broj_ocjena):
    lista_ocjena = []
    for i in range(broj_ocjena):
        naziv_predmeta  = input("unesite ime predmeta: ")
        predavac = input('Unesite ime predavaca: ')
        student = input("Ime studenta: ")
        ocjena = float(input("Unesite ocjenu"))
        print('-'*5)
        lista_ocjena.append({"naziv_predmeta": naziv_predmeta, 'predavac': predavac, 'student': student,'ocjena':ocjena})
    return lista_ocjena

def vrati_prosjek(ocjene, student):
    suma = 0
    broj = 0
    lista_student = []
    for i in ocjene:
        if i['student'] == student:
            lista_student.append(i)
            suma += i['ocjena']
            broj += 1
    return lista_student , suma / broj

s = unesi_ocjene(2)
print(vrati_prosjek(s,"marko"))