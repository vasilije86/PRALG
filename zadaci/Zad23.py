text = input("unesite text: ")
p = 1
for i in text:
    if i.isnumeric():
        p *= int(i)
print(p)