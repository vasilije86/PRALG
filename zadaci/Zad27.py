por = "yx*z#"
s = 1
for i in por:
    if i == "y":
        s+=2
    elif i == 'z':
        s *= 2
    elif i == "x":
        s -= 2
    elif i == '#':
        s **= 2
    elif i == "*":
        continue
print(por, s)
