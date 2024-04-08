def temp_convert(temps):
    return list(map(lambda x: (x[0], (9/5)*x[1]+32), temps))

l = [("Cetinje", 20), ('Podgorica', 22), ('Budva', 24)]
print(temp_convert(l))
