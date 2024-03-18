s = input("Unesi tekst: ")
r = ""
for i in s:
    if i.isupper() == True:
       r = r + i
print(r)