import csv 
import matplotlib.pyplot as plt

with open('pjesme.csv') as pjesme:
    sadrzaj = csv.DictReader(pjesme)
    zanrovi = {}
    for red in sadrzaj:
        zanrovi[red["Genre"]] = zanrovi.get(red["Genre"], 0) + 1
        
plt.figure(figsize=(10, 5))
plt.bar(zanrovi.keys(), zanrovi.values(), color='r')
plt.xlabel('Žanrovi')
plt.ylabel('Broj pjesama')
plt.title('Broj pjesama po žanru')
plt.xticks(rotation=90)
plt.show()
