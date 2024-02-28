#izracunaj povrsinu trougla ako su poznate koordinate njegovih tjemena
from math import sqrt


x1 = 3
y1 = 2
x2 = 6
y2 = 3
x3 = 4
y3 = 7

x = sqrt((x2-x1)**2+(y2-y1)**2)
y = sqrt((x3-x1)**2+(y3-y1)**2)
z = sqrt((x2-x3)**2+(y2-y3)**2)
s= (x+y+z)/2
sp = sqrt(s*(s-x)*(s-y)*(s-z))
print(sp) 