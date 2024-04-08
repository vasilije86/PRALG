import csv
year = 2017 #int(input("Unesite godinu"))
with open("cars.csv") as cars:
    data = csv.DictReader(cars)
    header = next(data)
    f2 = open("cars2.csv", "w", newline="")
    writer = csv.DictWriter(f2, fieldnames=header)
    for row in data:
        if int(row["year"]) >= year:
            writer.writerow(row)
    f2.close()
