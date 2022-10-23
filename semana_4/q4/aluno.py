# Aluno: Tulio Castro Silva

from pessoa import *
from notas import *

class aluno(pessoa,notas):
    def __init__(self,identidade, cpf, matricula, nota1, nota2 , nota3, nome= "", telefone= "", endereco = "", idade = 0):
        pessoa.__init__(self, identidade, cpf, nome ,telefone,endereco, idade) #Inicializando a classe pessoa
        notas.__init__(self,nota1,nota2,nota3) #Inicializando a classe notas 
        self.matricula = matricula
    
    def visualizarMedia(self):
        """Funcao que imprime a media"""
        print(round(self.calculaMedia(),1))