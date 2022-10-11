#Aluno: Tulio Castro Silva

class arquivo:
    def __init__(self,arquivo):
        self.arquivo = arquivo
    
    def alunos_6_notas(self):
        arq = open(self.arquivo)
        for linha in arq:
            checagem = linha.split(" ")
            if len(checagem) >= 7:
                print(checagem[0])
        arq.close()
    
    def media (self):
        arq = open(self.arquivo)
        for linha in arq:
            checagem = linha.split(" ",1)
            soma = checagem[1].split(" ")
            media_arimimetica = (sum(map(int,soma)))/len(soma)
            print("{} {}\n".format(checagem[0] , media_arimimetica))
        arq.close()
    
    def max_min(self):
        arq = open(self.arquivo)
        for linha in arq:
            checagem = linha.split(" ",1)
            numeros = checagem[1].split(" ")
            print("|{} maximo = {} minimo ={}|".format(checagem[0],max(numeros, key = int),min(numeros , key = int)))
        arq.close()

if __name__ == "__main__":
    teste = arquivo("notas.txt")
    print("--------------------")
    teste.alunos_6_notas()
    print("--------------------")
    teste.media()
    print("--------------------")
    teste.max_min()
                

        
