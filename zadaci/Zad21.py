b = int(input("do kojeg broja: "))
zp = 0
zn = 1
p = 0
n = 0
for i in range(1,b+1):
    if i % 2 == 0:
        p += 1
        zp += i
    elif i % 2 != 0:
        n += 1
        zn *= i
    i += 1
print(f"Zbir parnih:{zp}, broj parnih:{p}, zbir neparnih:{zn}, broj neparnih:{n}")