#Aluno:Tulio Castro Silva

def analise(arquivo):
    """Função que analisa um texto inserido, diz o numero de linhas, linhas em branco, numero de frases, palavras
    e caracteres, tambem analisa se o arquivo inserido e valido"""
    try:
        relatorio = open("relatorio.txt", "w")
        conteudo = open(arquivo,"r")
        num_linhas = 0
        num_frases = 0
        num_palavras = 0
        num_linhas_branco = 0
        num_caracteres = 0
        for linha in conteudo:
            num_linhas += 1
            linha = linha.lower()
            linha = linha.split(" ") # separando a linha nos espaços para determinar o numero de frases
            if linha == ["\n"]: # avaliando se a linha e uma linha em branco
                num_linhas_branco += 1
            else:
                num_palavras += len(linha) #numero de palavras numero de itens na lista separada com espacos 
                for palavra in linha:
                    num_caracteres += len(palavra) # contando o numero de caracteres 
                    for letra in palavra: # procurando pontos que indicam final de frase 
                        if letra in ".,!?":
                            num_frases += 1
        relatorio.write("Numero de linhas : {}\n".format(num_linhas))
        relatorio.write("Numero de frases : {}\n".format(num_frases))
        relatorio.write("Numero de palavras : {}\n".format(num_palavras))
        relatorio.write("Numero de linhas em branco : {}\n".format(num_linhas_branco))
        relatorio.write("Numero de paragrafos : {}\n".format(num_linhas_branco + 1))
        relatorio.write("Numero de caracteres : {}\n".format(num_caracteres))
    except FileExistsError:
        print("O arquivo inserido não existe, um arquivo com esse nome sera criado")
        conteudo = open(conteudo, "w")
    finally:
        relatorio.close()
        conteudo.close()

if __name__ == "__main__":
    analise("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_3/q5/conteudo.txt")