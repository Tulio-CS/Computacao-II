from pessoa import *

class professor(pessoa):
    def __init__(self, identidade, cpf, salario = 0, nome= str, telefone= str, endereco = str, idade = 0):
        pessoa.__init__(self, identidade, cpf, nome ,telefone,endereco, idade)
        if int(salario) < 0:
            raise("Salario invalido")
        self.__salario = salario
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,valor):
        if valor < 0:
            raise("Valor invalido")
        self.__salario = valor
