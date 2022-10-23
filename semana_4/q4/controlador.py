# Aluno: Tulio Castro Silva

from professor import *
from professorhorista import *
from aluno import *

class controller:
    def __init__(self,listaAlunos = [],listaProfessores = []):
        self.listaAlunos = listaAlunos
        self.listaProfessores = listaProfessores

    def incluirAluno(self,obj):
        """Funcao que insere um aluno na lista de alunos checa se o tipo inserido e valido"""
        if type(obj) == aluno:
            self.listaAlunos.append(obj)
        else:
            raise TypeError("Tipo de entrada invalido")

    def pesquisarAlunoPorNome(self,nome):
        """Funcao que pesquisa o aluno por nome"""
        for i in range(len(self.listaAlunos)):
            if self.listaAlunos[i].nome == nome:
                return self.listaAlunos[i]
            else:
                continue
        return False
    
    def pesquisarAlunoPorCPF(self,cpf):
        """Funcao que pesquisa o aluno pelo cpf"""
        for i in range(len(self.listaAlunos)):
            if self.listaAlunos[i].cpf == cpf:
                return self.listaAlunos[i]
            else:
                continue
        return False
    
    def incluirProfessor(self,obj):
        """Funcao que insere um professor na lista de alunos checa se o tipo inserido e valido"""
        if type(obj) == professor or type(obj) == professorHorista:
            self.listaProfessores.append(obj)
        else:
            raise TypeError("Tipo de entrada invalida")
    
    def pesquisarProfessorPorNome(self,nome):
        """Funcao que pesquisa o professor por nome"""
        for i in range(len(self.listaProfessores)):
            if self.listaProfessores[i].nome == nome:
                return self.listaProfessores[i]
            else:
                continue
        return False
    
    def pesquisarProfessorPorCPF(self,cpf):
        """Funcao que pesquisa o professor por cpf"""
        for i in range(len(self.listaProfessores)):
            if self.listaProfessores[i].cpf == cpf:
                return self.listaProfessores[i]
            else:
                continue
        return False

