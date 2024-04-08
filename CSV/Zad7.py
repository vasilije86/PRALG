import csv
import matplotlib.pyplot as plt

with open("cars.csv") as cars:
    data = csv.DictReader(cars)
    header = next(data)
    colors = {}
    for row in data:
        colors[row["color"]] = colors.get(row["color"], 0) + 1

color_list = []
for key, value in colors.items():
    color_list.append((value, key))

color_list.sort(reverse=True)
top5_colors = color_list[:5]
plt.pie([item[0] for item in top5_colors], labels=[item[1] for item in top5_colors])
plt.show()
f2 = open("top5_colors.csv", "w", newline="")
writer = csv.DictWriter(f2, fieldnames=["count", "color"])
for item in top5_colors:
    writer.writerow({"count": item[0], "color": item[1]})