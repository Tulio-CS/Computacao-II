#Aluno: Tulio Castro Silva

from q2 import *

"""
    Comentarios: 
    Quando é solicitada a representação da Classe Trabalhador horista
    a função calcularpagamento e chamada automaticamente, atualizando 
    o salario do funcionario
"""

if __name__ == "__main__":
    ########################################################
    tulio = TrabalhadorAssalariado("tulio","cpf do tulio")
    carol = TrabalhadorAssalariado("Carol","cpf da carol")
    hilda = TrabalhadorAssalariado("Hercules","cpf da hilza")
    azalim = TrabalhadorHorista("azalim","cpf do azalim")
    jhu = TrabalhadorHorista("jhu","cpf da jhu")
    vitor = TrabalhadorHorista("virto","cpf do virto")
    #######################################################
    tulio.definirSalario(-1)
    tulio.definirSalario(5)
    carol.definirSalario(10000)
    hilda.definirSalario(0.1)
    azalim.horasTrabalhadas = 0
    azalim.horasTrabalhadas = 80
    azalim.valorHoras = 30
    jhu.horasTrabalhadas = 100
    jhu.valorHoras = 2
    vitor.horasTrabalhadas = 22
    vitor.valorHoras = 42
    #######################################################
    trabalhadores = [tulio,carol,hilda,azalim,jhu,vitor]
    for i in range(len(trabalhadores)):
        print(trabalhadores[i])