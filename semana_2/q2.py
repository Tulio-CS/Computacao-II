#Aluno : Tulio Castro Silva


class Funcionario:
    def __init__(self,nome, cpf):
        """Iniciando a classe funcionario, com um determinado nome e cpf
        str, str -> obj"""
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = 0

    @property
    def nome(self):
        """Definindo a propriedade nome que nao pode ser alterado ou deletado"""
        return self.__nome
    
    @property
    def cpf(self):
        """Definindo a propriedade cpf que nao poded ser alterado ou deletado"""
        return self.__cpf

    @property
    def salario(self):
        """Definindo a propriedade nome que pode ser alterada """
        return (self.__salario)
    
    @salario.setter
    def salario(self,valor):
        """Definindo o metodo set da propriedade salario"""
        if valor > 0:
            self.__salario = valor
        else:
            print("Valor invalido")
    
    def __str__(self):
        """Representação do objeto da classe Funcionario
        obj -> str"""
        return ("{}\nNome : {}\nCPF : {}\nSalario : {}\n{}".format("-" *20,self.nome,self.cpf,self.salario,"-" *20))

class TrabalhadorAssalariado(Funcionario):
    def __init__(self,nome, cpf):
        """Iniciando a subclasse Trabalhador Assalariado
        str, str -> obj"""
        Funcionario.__init__(self,nome, cpf)
    
    def definirSalario(self,salario):
        """Função que define o atributo salario da classe Funcionario"""
        if salario > 0:
            self.salario = salario
        else:
            print("Valor invalido")

class TrabalhadorHorista(Funcionario):
    def __init__(self,nome, cpf, valorHoras = 0, horasTrabalhadas = 0):
        """Iniciando a classe Trabalhador Horista, subclasse da classe Funcionario
        str, str, int, int -> obj"""
        Funcionario.__init__(self,nome, cpf)
        self.__valorHoras = valorHoras
        self.__horasTrabalhadas = horasTrabalhadas
    
    @property
    def valorHoras(self):
        """Definindo a propriedade valor das horas do funcionario horista"""
        return self.__valorHoras
    
    @valorHoras.setter
    def valorHoras(self, valor):
        """Metodo set do atributo valor horas"""
        if valor > 0:
            self.__valorHoras = valor
        else:
            print("Valor invalido")

    
    @property
    def horasTrabalhadas(self):
        """Definindo a propriedade hroas trabalhadas"""
        return self.__horasTrabalhadas
    
    @horasTrabalhadas.setter
    def horasTrabalhadas(self,valor):
        """Metodo set do atributo horas trabalhadas"""
        if valor > 0:
            self.__horasTrabalhadas = valor
        else:
            print("Valor invalido")
    
    def __str__(self):
        """Representação especial da classe Trabalhador Horista
        calcula automaticamente o salario do funcionario"""
        self.calcularPagamento()
        return("{}\nNome : {}\nCPF : {}\nSalario : {}\n{}".format("-" *20,self.nome,self.cpf,self.salario,"-" *20))
    
    
    def calcularPagamento(self):
        """Função que calcula o salario do funcionario"""
        if self.__horasTrabalhadas == 0:
            return print("O atributo horas trabalhadas nao foi preenchido")
        elif self.__valorHoras == 0:
            return(print("O atributo valor horas nao foi preenchido"))
        else:
            self.salario = self.__valorHoras * self.__horasTrabalhadas
        





