a = input("unesi string: ")
r = ""
for i in a:
    if i.lower() in "aeiou":
        r = r + i
print(r)