#Aluno: Tulio Castro Silva

def tempos(arq):
    """Funcao que le um arquivo com nomes e tempos de corredores , analisam o melhor corredor e a melhor volta"""
    tempo_total = {} #dicionario com o nome do corredor e o tempo total 
    melhor_volta = {} #dicionario com o nome do corredor e sua melhor volta
    try:
        arquivo = open(arq,"r")
        for linha in arquivo.readlines():
            linha = linha.split("|") 
            linha[len(linha)-1] = linha[len(linha)-1].strip("\n") #removendo o \n do final da linha
            if len(linha) != 11: #tratando erros
                raise ValueError("Numero de voltas invalido")
            tempo_total["{}".format(linha[0])] = sum(map(int,(linha[1:]))) #adicionando o tempo total dos corredores
            melhor_volta["{}".format(linha[0])] = [min(linha[1:],key = int),linha.index(min(linha[1:],key = int))] #adicionando a melhor volta de cada corredor ao dicionario 
        mv = min(melhor_volta, key= melhor_volta.get) #lista com o melhor corredor e sua melhor volta
        melhor_tempo = min(tempo_total, key = tempo_total.get) #lista com corredor com o melhor tempo
        print(melhor_tempo)
        print("O corredor {} teve a melhor volta com {} segundos, esta foi sua {} volta".format(mv,melhor_volta[mv][0],melhor_volta[mv][1]))
        print("O corredor {} teve o melhor tempo e seu tempo total foi {} segundos".format(melhor_tempo,tempo_total[melhor_tempo]))
    except FileNotFoundError:
        raise NameError("Arquivo invalido")




tempos("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_5/q5/tempos.txt")