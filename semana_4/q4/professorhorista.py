# Aluno: Tulio Castro Silva

from professor import *

class professorHorista(professor):
    def __init__(self, identidade, cpf, valorHora, horasTrabalhadas, nome= "", telefone= "", endereco = "", idade = 0):
        professor.__init__(self,identidade,cpf,0,nome,telefone,endereco,idade)
        # professor.__init__(self, identidade, cpf, nome, telefone, endereco , idade)        
        if valorHora < 0:
            raise ValueError("Valor da hora invalido")
        if horasTrabalhadas < 0:
            raise ValueError("Valor para horas trabalhadas invalido")
        self.__valorHora = valorHora
        self.__horasTrabalhadas = horasTrabalhadas
    
    @property
    def valorHora(self):
        """Property valor hora"""
        return self.__valorHora
    
    @valorHora.setter
    def valorHora(self,valor):
        """Valor hora setter checa se o valor inserido e valido"""
        if valor < 0:
            raise ValueError("Valor invalido")
        self.__valorHora = valor
    
    @property
    def horasTrabalhadas(self):
        """Property horas trabalhadas"""
        return self.__horasTrabalhadas
    
    @horasTrabalhadas.setter
    def horasTrabalhadas(self,valor):
        """Horas trabalhadas setter checa se o valor inserido e valido"""
        if valor < 0:
            raise ValueError("Valor invalido")
        self.__horasTrabalhadas = valor
    
    def calcularSalario(self):
        """Funcao que calcula o salario"""
        valor = self.valorHora * self.horasTrabalhadas
        self.salario = valor
    