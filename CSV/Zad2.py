import csv
import csv
# Napisi u fajl samo ID, ime i danceability
with open('pjesme.csv') as pjesme:
    sadrzaj = csv.DictReader(pjesme)
    head = next(sadrzaj)

    pjesme = []
    for red in sadrzaj:
        pjesme.append(red)
    pjesme.sort(key=lambda x: x["Danceability"], reverse=True)

    newfile = open("zadatak2.csv", 'w', newline='')
    fieldnames = ["ID", "Track.Name", "Danceability"] 
    writer = csv.DictWriter(newfile, fieldnames=fieldnames)
    writer.writeheader()
    for pjesma in pjesme[:10]:
        info = {"ID": pjesma["ID"], "Track.Name": pjesma["Track.Name"], "Danceability": pjesma['Danceability']} 
        writer.writerow(info)
    newfile.close()

