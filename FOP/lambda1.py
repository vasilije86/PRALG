def kvadriraj(i):
    return i*i
# print(kvadriraj(3))

kvadriraj_lambda = lambda x: x*x
# print(kvadriraj_lambda(3))

# def build_quadratic(a,b,c):
#     return lambda x : a*x*x + b*x + c
# func = build_quadratic(3,2,1)
# print(func(0)) # Returns the x value 
# print(func(1)) # Returns the first variable
# print(func(2))
# print(build_quadratic(3,2,1)(2))

def even_check(num):
    if num % 2 ==0:
        return True
    else:
        return False
    #return num % 2
# even_check_lambda = lambda x: x %2 ==0
l = [2,5,4,3,6,10]
print(list(map(lambda x:x+1, list(filter(lambda x: x %2 ==0, l))))) # Map 1st arg: func we want to do, 2nd: item we iterate over


