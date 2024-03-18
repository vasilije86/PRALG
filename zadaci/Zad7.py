x1 = 2
y1 = 3
x2 = 7
y2 = 9
x3 = x2 + 2
y3 = y2 - 3
# hrast do blaga
dist = ((x3-x1)**2 + (y3-y1)**2)**0.5
#hrst do kuce
dist1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
# kuca do blaga
dist2 = ((x3-x2)**2 + (y3-y2)**2)**0.5
print(f"vazduzna linija duzina {dist}")
print(f"Obici i kucu {dist1+dist2}")