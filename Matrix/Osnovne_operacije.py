# Kreiranje matrice
# m = [[1,2],[3,4]]

# Kreiranje 0 kvadratne matrice
vel =  3 # int(input("Unesi dimenziju: "))
kvadratna = [[0 for i in range(vel)] for i in range(vel)]

# for i in kvadratna:
#     print(i)

# Azuriraj da elementi diagonale budu `1`
for i in range(vel):
    kvadratna[i][i] = 1
#     for j in range(vel):
#         if i == j:
#             kvadratna[i][j] = 1
# for i in kvadratna:
#     print(i)

# Stampati sve elemente matrice redom (vrsta -> kolona)
# for i in range(vel):
#     for j in range(vel):
#         print(kvadratna[i][j])
# print(*[kvadratna[i][j] for i in range(vel) for j in range(vel)])
            
# Saberi sve elemente matrice
# sum = 0
# for i in range(vel):
#     for j in range(vel):
#         sum += kvadratna[i][j]
# print(sum)

# 