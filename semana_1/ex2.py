class Funcionario():
    def __init__(self,nome,departamento,salario,data_entrada,cpf,ativo):
        self.nome = nome
        self.departamento = departamento
        self.salario = salario
        self.data_entrada = data_entrada
        self.cpf = cpf
        self.ativo = ativo
    
    def bonificar(self,valor):
        """Funcao que aumenta o salario de determinado funcionario caso este esteja ativo na empresa"""
        if self.ativo == True:
            self.salario += valor
        else:
            print("Esse funcionario ja foi demitido")
        
    def demitir (self):
        """Funcao que demite determinado funcionario"""
        if self.ativo == True:
            self.ativo = not(self.ativo)
        else:
            print("Esse funcionario ja foi demitido") 
    
jorge = Funcionario("Jorge","ri",100,"25/12/2004","10677777710",True)

jorge.bonificar(101)
print(jorge.salario)
print(jorge.ativo)
jorge.demitir()
jorge.bonificar(102)
print(jorge.ativo)