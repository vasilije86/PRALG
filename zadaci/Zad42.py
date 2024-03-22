def ponavljanje(file):
    f = open(file, "r")
    linija  = f.read().split("\n")
    f.close()
    counts = dict()
    for line in linija:
        words = line.split()
        for word in words:
            word = word.lower()
            counts[word] = counts.get(word, 0) + 1
    return print(counts)

ponavljanje("C:/Users/vasil/Documents/Fax/4.semestar/PRALG/PRALG/zadaci/text.txt")