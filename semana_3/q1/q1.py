#Aluno: Tulio Castro Silva



def copia (arq1, arq2):
    """Esta funcao tenta abrir um arquivo e cirar uma copia do mesmo 
    excluindo as linhas comecadas com #, se falhar retorna uma mensagem de erro"""
    try:
        """tratando o erro de o arquivo inserido nao existir"""
        arquivo1 = open(arq1 , "r")
        arquivo2 = open(arq2 , "w")
        for linha in arquivo1:
            if linha[0] == "#":
                continue
            else:
                arquivo2.write(linha)
    except FileNotFoundError:
        print("O arquivo inserido não existe, um arquivo com esse nome sera criado")
        arquivo1 = open(arq1 , "w")
    finally:
        arquivo1.close()
        arquivo2.close()


if __name__ == "__main__":
    copia("teste.txt","copia.txt")
