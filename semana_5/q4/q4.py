#Aluno: Tulio Castro Silva

def contar(arquivo):
    """Funcao que calcula o numero de vogais de um texto
    file -> dict"""
    vogais = {"a":0,"e":0,"i":0,"o":0,"u":0}
    try:
        arq = open(arquivo,"r")
        for linha in arq:
            linha = linha.lower()
            for letra in linha:
                if letra in "aeiou":
                    vogais[letra] += 1
        for keys, values in vogais.items():
            print("{} = {}".format(keys,values))
    except FileNotFoundError:
        raise NameError("Arquivo invalido")

contar("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_5/q4/texto.txt")
