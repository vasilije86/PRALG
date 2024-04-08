from functools import reduce
a = [1,4,3,2]
print(reduce(lambda x,y: x+y, a))