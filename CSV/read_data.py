import csv

def load_data(filename):
    item_list = []
    with open(filename) as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # skip csv header
        for row in csv_data:
            item_list.append(row)
        return item_list
    
new_list = load_data("google_stock_data.csv")
for i in range(3):
    print(new_list[i])


