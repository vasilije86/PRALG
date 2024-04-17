class Pravouganoik():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def povrsina(self):
        return self.__a * self.__b
    
    def obim(self):
        return 2 * (self.__a + self.__b)
p1 = Pravouganoik(2,3)
print(p1.__a)