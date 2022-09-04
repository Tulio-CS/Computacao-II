class Elevador:
    def __init__(self,capacidade,total_andares,tripulantes = 0,andar_atual = 0) :
        self.capacidade = capacidade
        self.total_andares = total_andares
        self.tripulantes = tripulantes
        self.andar_atual = andar_atual
    def entrar(self):
        if self.tripulantes < self.capacidade:
            print("uma pessoa entrou")
            self.tripulantes += 1
        else:
            print("A capacidade maxima ja foi atingida")
    def sair(self):
        if self.tripulantes > 0:
            print("uma pessoa saiu do elevador")
            self.tripulantes -= 1
        else:
            print("Ninguem esta usando o elevador no momento")
    def sobe(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print("O elevador subiu um andar o andar atual é {}".format(self.andar_atual))
        else:
            print("O elevador ja esta no seu ultimo andar")
    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print("O elevador desceu um andar o andar atual é {}".format(self.andar_atual))
        else:
            print("O elevador ja esta no terreo")
def main(self):
    print("-"*10)
    print("andar atual => {}\ntripulantes ->{}\ncapacidade total -> {}\nnumero de andares ->{}".format(self.andar_atual,self.tripulantes,self.capacidade,self.total_andares))
elevador1 = Elevador(10,3)

main(elevador1)

elevador1.desce()

main(elevador1)


