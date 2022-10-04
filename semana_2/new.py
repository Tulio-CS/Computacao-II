class funcionarios:
    def __init__(self, nome, cpf):
        self.__nome=nome
        self.__cpf=cpf
        self.__salario = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf 

    @property
    def salario(self):
        return self.__salario 

    @salario.setter
    def salario(self, x):
        if x<0:
            print('Esse valor é invalido')
        else:
            self.__salario = x
    def __str__(self):
        """Representação do objeto da classe Funcionario
        obj -> str"""
        return ("{}\nNome : {}\nCPF : {}\nSalario : {}\n{}".format("-" *20,self.nome,self.cpf,self.salario,"-" *20))


class trabalhadorAssalariado (funcionarios):
    def __init__ (self, nome, cpf):
        funcionarios.__init__(self, nome, cpf)

    def definir_salario (self, salario):
        if salario > 0:
            self.salario = salario
        else:
            print('Esse valor não é valido')


class trabalhadorHorista (funcionarios):
    def __init__ (self, nome, cpf, valor, horas):
        funcionarios.__init__(self, nome, cpf)
        self.__valor = valor
        self.__horas = horas

    @property
    def valor (self):
        return self.__valor

    @valor.setter
    def valor (self, valor):
        if valor > 0:
            self.__valor = valor
        else:
            print ('Esse valor não é valido')

    @property
    def horas (self):
        return self.__horas

    @horas.setter
    def horas (self, hora):
        if hora > 0:
            self.__horas = hora
        else:
            print('Esse valor não é valido')

    def calcula_pagamento(self):
        self.salario = self.__valor * self.__horas
        print(self.salario)
        
    def __str__(self):
        self.calcula_pagamento()
        return("{}\nNome : {}\nCPF : {}\nSalario : {}\n{}".format("-" *20,self.nome,self.cpf,self.salario,"-" *20))
        


#########################################################

t = trabalhadorHorista("nome","cpf",10,15)
print(t)