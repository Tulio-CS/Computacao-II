#Aluno:Tulio Castro Silva

def analise(arquivo):
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
        linha = linha.split(" ")
        if linha == ["\n"]:
            num_linhas_branco += 1
        else:
            num_palavras += len(linha)
            for palavra in linha:
                num_caracteres += len(palavra)
                for letra in palavra:
                    if letra in ".,!?":
                        num_frases += 1
    relatorio.write("Numero de linhas : {}\n".format(num_linhas))
    relatorio.write("Numero de frases : {}\n".format(num_frases))
    relatorio.write("Numero de palavras : {}\n".format(num_palavras))
    relatorio.write("Numero de linhas em branco : {}\n".format(num_linhas_branco))
    relatorio.write("Numero de paragrafos : {}\n".format(num_linhas_branco + 1))
    relatorio.write("Numero de caracteres : {}\n".format(num_caracteres))
    relatorio.close()
    conteudo.close()

if __name__ == "__main__":
    analise("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_3/q5/conteudo.txt")