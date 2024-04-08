import csv

with open('pjesme.csv') as pjesme:
    sadrzaj = csv.DictReader(pjesme)
    header = next(sadrzaj)
    print(header)
    
    pjesme = []
    for red in sadrzaj:
        pjesme.append(red)


    pjesme.sort(key = lambda x:x["Length."], reverse=True )

    f2 = open("zadatak1.csv", 'w', newline='')
    pisanje = csv.DictWriter(f2,header )
    pisanje.writeheader()
    pisanje.writerows(pjesme[:10])
    f2.close()