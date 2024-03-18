import math

x_strelice = 2
y_strelice = 3

cx_tabla = 6
cy_tabla = 7

poluprecnik_tabla = 5

udaljenost = math.sqrt((x_strelice - cx_tabla)**2 + (y_strelice - cy_tabla)**2)

if udaljenost <= poluprecnik_tabla:
    print("Strelica je pogodila pikado tablu.")
else:
    print("Strelica nije pogodila pikado tablu.")
