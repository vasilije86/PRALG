import matplotlib.pyplot as plt # Koristimo samo pyplot iz  matplot lib

# x = [0,1,2,3,4]
# y = [0,2,4,6,8]

# plt.figure(figsize=(5,3)) # Odredi velicinu prostora za prikaz diagrama
# plt.plot(x,y,label="2x", color='r', linewidth=1, linestyle='-', marker='*',markersize=5) # za punu liniju - ,za isprekidanu --, za ostlo pogledaj dokumentaciju

# x2 = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5]
# y1 = [e ** 2 for e in x2[:6]]
# y2 = [e ** 2 for e in x2[5:]]

# plt.plot(x2[:6],y1, label='x**2', color='b', linewidth=1)
# plt.plot(x2[5:],y2, linestyle="--")
# plt.xlabel("X osa")
# plt.ylabel("Y osa")



# plt.legend() # Kreira legend za dodate argumente
# plt.title("Prva funkcija", fontdict={'fontname': 'Arial', 'fontsize': 15})
# # plt.savefig('funkcija.png') # Ne treba plt.show poslije ovoga, pravi png i cuva u isti directory kao i .py fajl
# plt.show()

# Kretanje cijena akcija
dates = ['Jan 1','Jan 2','Jan 3','Jan 4','Jan 5','Jan 6','Jan 7']
stock_price = [12,13,15,18,20,22,25]

plt.plot(dates,stock_price)
plt.xlabel("Datum")
plt.ylabel("Cijene Akcija")
plt.title("Kretanje Akcija")

plt.show()

