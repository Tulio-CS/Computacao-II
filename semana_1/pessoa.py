class Pessoa():

    def __init__(self,nome,sexo,cpf,conjuge="sem conjuge"):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.conjuge = conjuge

    def informaConjuge(self):
        """Função que informa o nome do conjuge do objeto pessoa caso o mesmo exista"""
        if self.conjuge != "sem conjuge":
            print(self.conjuge.nome)
        else:
            print("{} não é casada".format(self.nome))
    
    def casar(self,pessoa):
        """Altera o conjuge do objeto pessoa caso o mesmo não seja casado"""
        if self.conjuge == "sem conjuge" and pessoa.conjuge == "sem conjuge":
            self.conjuge = pessoa
            pessoa.conjuge = self
        else:
            print("Erro, não foi possivel realisar este casamento")


Tulio = Pessoa("tulio","homem","10666")
Bruno = Pessoa("Bruno","homem","10523")

