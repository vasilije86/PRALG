import csv
with open("cars.csv") as cars:
    data = csv.DictReader(cars)
    header = next(data)
    avg_price = {}
    count = {}
    brand=  {}

    for row in data:
        count[row["brand"]] = count.get(row["brand"], 0) + 1
        brand[row["brand"]] = brand.get(row["brand"], 0) + float(row["price"])

for key in brand:
    avg_price[key] = brand[key] / count[key]
print(avg_price)