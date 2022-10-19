from professor import *

class professorHorista(professor):
    def __init__(self, identidade, cpf, valorHora, horasTrabalhadas, nome= "", telefone= "", endereco = "", idade = 0):
        professor.__init__(self,identidade,cpf,0,nome,telefone,endereco,idade)
        # professor.__init__(self, identidade, cpf, nome, telefone, endereco , idade)        
        if valorHora < 0:
            raise("Valor da hora invalido")
        if horasTrabalhadas < 0:
            raise("Valor para horas trabalhadas invalido")
        self.__valorHora = valorHora
        self.__horasTrabalhadas = horasTrabalhadas
    
    @property
    def valorHora(self):
        return self.__valorHora
    
    @valorHora.setter
    def valorHora(self,valor):
        if valor < 0:
            raise("Valor invalido")
        self.__valorHora = valor
    
    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @horasTrabalhadas.setter
    def horasTrabalhadas(self,valor):
        if valor < 0:
            raise("Valor invalido")
        self.__horasTrabalhadas = valor
    
    def calcularSalario(self):
        valor = self.valorHora * self.horasTrabalhadas
        self.salario = valor
    