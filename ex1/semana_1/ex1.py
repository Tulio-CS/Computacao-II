class Veiculo:

    def __init__(self,cons_comb,cap_comb):
        """Metodo construtor da classe veiculo"""
        self.cons_comb = cons_comb
        self.cap_comb = cap_comb
        self.qtd_comb = 0.0
    
    def mover(self,km):
        """funcao que verifica se o automovel possui combustivel para locomover determinada kilometragem
        em caso afirmativo ela anda com o veiculo e diminui sua quantidade de combustivel"""
        if (self.qtd_comb * self.cons_comb) >= km:
            self.qtd_comb -= (km * self.cons_comb)
            print("o veiculo andou {}".format(km))
        else:
            print("Não ha combustivel suficiente")

    def getCombustivel(self):
        """Funcao que retorna a quantidade de combustivel do veiculo"""
        return self.qtd_comb

    def abastecer(self,litros):
        """Funcao que aumenta a quantidade de combustivel do veiculo, sem deixar ultrapassar a quantidade maxima"""
        if litros > 0 :
            if self.qtd_comb + litros <= self.cap_comb:
                self.qtd_comb += litros
            else:
                print("Não é possivel abastecer essa quantidade de combustivel no veiculo")
        else:
            print("A quantidade desejada não e valida")
    
carro = Veiculo(10,101)

carro.abastecer(-1)
print(carro.getCombustivel())
carro.abastecer(100)
print(carro.getCombustivel())
carro.mover(10)
print(carro.getCombustivel())

    


        