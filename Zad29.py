recenica = "Dosadno mi AAbbCC je na FAX"

def maxuppper(recenica):
    count = 0
    maxcount = 0
    maxrijec = ""
    lista = list()
    for i in recenica.split(" "):
        
        for s in i:
            print(i, s)
            if s.isupper():
                count +=1
        if count > maxcount:
            maxcount = count
            maxrijec = i
        count = 0
    print(maxrijec, lista)
maxuppper(recenica)