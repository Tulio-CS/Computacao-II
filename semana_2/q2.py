class Funcionario:
    def __init__(self,nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = 0
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf

    @property
    def salario(self):
        return (self.__salario)
    
    @salario.setter
    def salario(self,valor):
        self.__salario = valor
    
    def __str__(self):
        return("Nome : {}\nCPF : {}\nSalario : {}".format(self.__nome,self.__cpf,self.__salario))

class TrabalhadorAssalariado(Funcionario):
    def __init__(self,nome, cpf):
        Funcionario.__init__(self,nome, cpf)
    
    def definirSalario(self,salario):
        self.salario = salario

class TrabalhadorHorista(Funcionario):
    def __init__(self,nome, cpf, valorHoras = 0, horasTrabalhadas = 0):
        Funcionario.__init__(self,nome, cpf)
        self.__valorHoras = valorHoras
        self.__horasTrabalhadas = horasTrabalhadas
    
    @property
    def valorHoras(self):
        return self.__valorHoras
    
    @valorHoras.setter
    def valorHoras(self, valor):
        self.__valorHoras = valor

    
    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @horasTrabalhadas.setter
    def horasTrabalhadas(self,valor):
        self.__horasTrabalhadas = valor
    
    
    def calcularPagamento(self):
        if self.__horasTrabalhadas == 0:
            return print("O atributo horas trabalhadas nao foi preenchido")
        elif self.__valorHoras == 0:
            return(print("O atributo valor horas nao foi preenchido"))
        else:
            self.salario = self.__valorHoras * self.__horasTrabalhadas
            return print("O salario deste mes foi {} reais".format(self.salario))
        


tulio = TrabalhadorAssalariado("tulio","cpf")
tulio.salario = 10
azalim = TrabalhadorHorista("azalim","cpf")
azalim.horasTrabalhadas = 10
azalim.valorHoras = 10
azalim.calcularPagamento()
print(tulio)
print(azalim)


