def brojevi(fajl):
    f= open(fajl, 'r').split('\n')
    f.close()
    suma = 0
    for broj in f:
        print(broj)
        if broj.startswith("Ox"):
            num = int(broj,16)
            if num %10 ==3:
                sum += num
    return print(sum)

brojevi('nums.txt')
