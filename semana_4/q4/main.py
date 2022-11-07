# Aluno: Tulio Castro Silva

from pessoa import *
from professor import * 
from professorhorista import *
from aluno import *
from controlador import *

if __name__ == "__main__":
    con = controller()
    tulio = aluno("000000001","00000000001","matricula-tulio",10,8,9,nome="Tulio",telefone="Telefone Tulio",idade=18)
    vitinho = aluno("000000002","00000000002","matricula-vitinho",7,5,8,telefone="Telefone do vitinho",nome="Vitinho")
    avellar = aluno("000000003","00000000003","matricula-avellar",8,8,8,nome="Avellar")
    con.incluirAluno(tulio)
    con.incluirAluno(vitinho)
    con.incluirAluno(avellar)
    bruno = professorHorista("000000004","00000000004",10,1,nome="bruno")
    leonardo = professor("000000005","00000000005",2500,nome="leonardo")
    dennis = professor("000000006","00000000006",1500,nome="dennis")
    con.incluirProfessor(bruno)
    con.incluirProfessor(leonardo)
    con.incluirProfessor(dennis)
    (con.pesquisarAlunoPorCPF("00000000001").visualizarMedia())
    (con.pesquisarAlunoPorCPF("00000000002").visualizarMedia())
    bruno.calcularSalario()
    print(con.pesquisarProfessorPorNome("bruno").salario)
    con.pesquisarAlunoPorCPF("cpfinexistente")
        