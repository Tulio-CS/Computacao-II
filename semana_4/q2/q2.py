# Aluno: Tulio Castro Silva

class Idades:
    def __init__(self, lista = []):
        """Iniciando a classe idades, inicia uma lista vazia se nenhum valor é inserido ou se a lista contem strings"""
        if type(lista) != list: 
            raise Exception("Tipo de entrada invalido")
        else:
            self.__listaidades = sorted(lista)
            for i in lista:
                if isinstance(i,int) and i > 0:
                    continue
                else:
                    print("erro na inicialização da lista, uma string foi encontrada, inicializando lista vazia")
                    self.__listaidades = []
                    
    def inserir_idades(self,idade):
        """Funcao que insere uma idade na lista se possivel"""
        if isinstance(idade,int) and idade > 0:
            self.__listaidades.append(idade)
        else:
            raise TypeError("Tipo inserido invalido")
    
    def media(self):
        """Funcao que retorna a meda da lista de idades
        -> int"""
        return (sum(self.__listaidades))/len(self.__listaidades)

    def __str__(self):
        print("Idades :")
        for i in range(len(self.__listaidades)):
            print(self.__listaidades[i])
        return "-------"

if __name__ == "__main__":
    i = Idades()
    i.inserir_idades("10")
    i.inserir_idades(10)
    i.inserir_idades(20)
    i.inserir_idades(11)
    i.inserir_idades(21)
    print("A media das idedes é {}".format(i.media()))
    print(i)