
def tempos(arq):
    tempo_total = {}
    melhor_volta = {}
    try:
        arquivo = open(arq,"r")
        for linha in arquivo.readlines():
            linha = linha.split("|")
            linha[len(linha)-1] = linha[len(linha)-1].strip("\n")
            if len(linha) != 11:
                raise ValueError("Numero de voltas invalido")
            tempo_total["{}".format(linha[0])] = sum(map(int,(linha[1:])))
            melhor_volta["{}".format(linha[0])] = [min(linha[1:],key = int),linha.index(min(linha[1:],key = int))]
        mv = min(melhor_volta, key= melhor_volta.get)
        melhor_tempo = min(tempo_total, key = tempo_total.get)
        print(melhor_tempo)
        print("O corredor {} teve a melhor volta com {} segundos, esta foi sua {} volta".format(mv,melhor_volta[mv][0],melhor_volta[mv][1]))
        print("O corredor {} teve o melhor tempo e seu tempo total foi {} segundos".format(melhor_tempo,tempo_total[melhor_tempo]))
    except FileNotFoundError:
        raise NameError("Arquivo invalido")




tempos("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_5/q5/tempos.txt")