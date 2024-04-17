class Pravouganoik():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def povrsina(self):
        return self.a * self.b
    
    def obim(self):
        return 2 * (self.a + self.b)

class Kvadrat(Pravouganoik):
    def __init__(self, a, boja):
        super().__init__(a,a)
        self.boja = boja
    
    def fill(self):
        return f"Kvadrat je obojan sa bojom: {self.boja}"

k1  = Kvadrat(5, "plava")
print(k1.fill(), '\n',k1.povrsina())