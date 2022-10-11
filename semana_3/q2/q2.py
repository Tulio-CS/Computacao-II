#Aluno: Túlio Castro Silva

def ip (arquivo):
    """Função que recebe um arquvivo contendo uma lista de ips e retorna uma copia
    dizendo se o ip e valido ou nao"""
    try:
        """tratando o erro de o arquivo inserido nao existir"""
        ips = open(arquivo, "r")
        relatorio = open("relatorio_ips.txt" , "w")
        for linha in ips:
            checagem = linha.split(".") #separando os numeros do ip nos pontos
            if checagem[0] >= "1"and checagem[0] <= "255" and checagem[1] >= "0" and checagem[1] <= "255" and checagem[2] >= "0" and checagem[2] <= "255" and checagem[3] >= "0" and checagem[3] <= "255":
                relatorio.write(str(linha).rstrip("\n") + " |IP valido|\n")
            else:
                relatorio.write(str(linha).rstrip("\n") + " |IP invalido|\n")
        ips.close()
        relatorio.close()
    except FileNotFoundError:
        print("O arquivo inserido não existe")

if __name__ == "__main__":
    ip("ip.txt")

    

