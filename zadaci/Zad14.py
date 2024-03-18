sp = int(input("prisustvo studenta: "))
ss = int(input("Jesu li seminarski uradjeni (0 ili 1): "))
if sp > 75 and ss == 1:
    print("Student moze pristupit ispitu")
else:
    print('student ne moze pristupit ispitu')