#Pronadji najduzi substring velikih slova
s = "AAbbCCC"
sub = ""
sub2 = ""

for char in s:
    if char.isupper():
        sub += char
    else:
        if len(sub) > len(sub2):
            sub2 = sub
        sub = ""

    
    if len(sub) > len(sub2):
        sub2 = sub
print(sub2)