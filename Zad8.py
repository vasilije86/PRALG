s = 0
p = 1
broj = int(input("Unesite trocifreni parni broj: "))
if broj %2 == 0 and 99<broj<1000:
    c1 = broj //100
    c2 = (broj //10) % 10 
    c3 = broj % 10
    if c1 % 2 ==0:
        s += c1
    if c2 %2 ==0:
        s += c2
    if c3 %2 ==0:
        s += c3  
broj2 = int(input("Unesite cetvorocifreni neparni: "))
if broj2 %2 != 0 and 999< broj2 < 10000:
    c4 = broj2 //1000
    c5 = (broj2 //100) % 10 
    c6 = (broj2 //10) % 10
    c7 = broj2 % 10
    if c4 % 2 !=0:
        p *= c4 
    if c5 %2 !=0:
        p *= c5 
    if c6 %2 !=0:
        p *= c6
    if c7 % 2 != 0:
        p *= c7    
if p > 1 and  p> s :
    print("Da")
else:
    print("Ne")