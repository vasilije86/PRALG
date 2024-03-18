start = int(input("unesite pocetni broj"))
end= int(input("unesite zadnji broh")) 
s = 0
for i in range(start, end+1):
    if i % 2== 0 and i%4 !=0:
        s += i**2
print(s)