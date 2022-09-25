class test:
    def __init__(self,teste):
        self.__teste = teste
    

    @property
    def teste(self):
        return self.__teste
    
    @teste.setter
    def teste(self, v):
        self.__teste = v

t = test("t")

print(t.teste)
t.teste = "u"
print(t.teste)