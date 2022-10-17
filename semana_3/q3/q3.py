#Aluno: Tulio Castro Silva

class arquivo:
    def __init__(self,arquivo):
        self.__arquivo = arquivo
    
    @property 
    
    def arquivo(self):
        return self.__arquivo
    
    @arquivo.setter

    def arquivo(self,new):
        self.__arquivo = new
        
    def alunos_6_notas(self):
        try:
            arq = open(self.arquivo, "r")
            for linha in arq:
                checagem = linha.split(" ")
                if len(checagem) >= 7:
                    print(checagem[0])
        except FileNotFoundError:
            print("O arquivo inserido não existe, um arquivo com esse nome sera criado")
            arq = open(self.arquivo, "w")
        finally:
            arq.close()

    
    def media (self):
        try:
            arq = open(self.arquivo, "r")
            for linha in arq:
                checagem = linha.split(" ",1)
                soma = checagem[1].split(" ")
                media_arimimetica = (sum(map(int,soma)))/len(soma)
                print("{} {}\n".format(checagem[0] , media_arimimetica))
        except FileNotFoundError:
            print("O arquivo inserido não existe, um arquivo com esse nome sera criado")
            arq = open(self.arquivo, "w")
        finally:
            arq.close()
        
    def max_min(self):
        try:
            arq = open(self.arquivo, "r")
            for linha in arq:
                checagem = linha.split(" ",1)
                numeros = checagem[1].split(" ")
                print("|{} maximo = {} minimo ={}|".format(checagem[0],max(numeros, key = int),min(numeros , key = int)))
        except FileNotFoundError:
            print("O arquivo inserido não existe, um arquivo com esse nome sera criado")
            arq = open(self.arquivo, "w")
        finally:
            arq.close()

if __name__ == "__main__":
    teste = arquivo("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_3/q3/notas.txt")
    print("--------------------")
    teste.alunos_6_notas()
    print("--------------------")
    teste.media()
    print("--------------------")
    teste.max_min()
                

        
