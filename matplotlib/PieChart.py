import matplotlib.pyplot as plt

x = {"Dogs": 20, 'Cats': 15, "Other": 5}

plt.pie(x.values(),labels=x.keys())

plt.show()