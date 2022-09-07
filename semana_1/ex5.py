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
        if self.conjuge == "sem conjuge":
            self.conjuge = pessoa
            pessoa.conjuge = self
        else:
            print("{} ja é casada".format(self.nome))


Tulio = Pessoa("Tulio","male","cpf")
Carol = Pessoa("Carol","fem","cpf")
Vini = Pessoa("Vini","male","1006")
Tulio.informaConjuge()
Tulio.casar(Carol)
Tulio.informaConjuge()
Carol.informaConjuge()
Carol.casar(Vini)
Carol.informaConjuge()





