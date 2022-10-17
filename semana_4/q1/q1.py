# Aluno: Tulio Castro Silva

class Pessoas:
    def __init__(self, lista = []):
        """Iniciando a classe pessoas, inicia uma lista vazia se nenhum valor é inserido"""
        if type(lista) != list: 
            print("O item inserido nao e uma lista, inicializando uma lista vazia")
            self.__listanomes = []
        else:
            self.__listanomes = sorted(lista)
    
    def inserir(self,nome):
        """Insere um ou mais nomes na lista, analisa se o argumento e uma lista ou uma string"""
        if type(nome) == list:
            for i in range(len(nome)):
                self.__listanomes.append(nome[i])
        else:
            self.__listanomes.append(nome)
        self.__listanomes = sorted(self.__listanomes)

    def consulta(self,index):
        """Consulta o index na lista, relata um erro se o index for maior do que a lista"""
        try:
            return self.__listanomes[index]
        except IndexError:
            print("O valor inserido ultrapassa o tamanho da lista")

    def __str__(self):
        print("-------")
        for i in range(len(self.__listanomes)):
            print(self.__listanomes[i])
        return "-------"


if __name__ == "__main__":
    listap = Pessoas(["tulio"])
    listap.inserir("tiago")
    print(listap.consulta(1))
    print(listap)
