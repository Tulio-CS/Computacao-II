# Aluno: Tulio Castro Silva

from pessoa import *

class professor(pessoa):
    def __init__(self, identidade, cpf, salario = 0, nome= str, telefone= str, endereco = str, idade = 0):
        pessoa.__init__(self, identidade, cpf, nome ,telefone,endereco, idade) #inicializando a classe pessoa
        if int(salario) < 0:
            raise ValueError("Salario invalido")
        self.__salario = salario
    
    @property
    def salario(self):
        """Propperty salario"""
        return self.__salario
    
    @salario.setter
    def salario(self,valor):
        """Salario setter checa se o valor inserido e valido"""
        if valor < 0:
            raise ValueError("Valor invalido")
        self.__salario = valor
