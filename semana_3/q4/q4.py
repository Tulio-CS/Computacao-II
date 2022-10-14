#Aluno: Tulio Castro Silva

import os

def tamanho(caminho):
    """Funcao que calcula o tamanho de um diretorio e seus subdiretorios dado um caminho
    retorna um html"""
    resultado = open("index.html", "w",encoding="utf-8") #Criando o html

    tamanho_diretorio = 0

    subdiretorios = [] #Fazendo uma lista com os subdiretorios 

    for root, diretorios, arquivos in os.walk(caminho):
        """Buscando os subdiretorios no diretorio"""
        for nome in arquivos:
            """Conseguindo os arquivos no subdiretorio"""
            subdiretorio = os.path.join(root, nome)
            subdiretorios.append("{}{}|tamanho = {} bytes|".format(subdiretorio,("-"*(130-len(subdiretorio))),os.path.getsize(subdiretorio)))
            tamanho_diretorio += os.path.getsize(subdiretorio)

    #Criando o inicio do html
    resultado.write('<!DOCTYPE html>\n<html lang="pt-br">\n<style>\n    body {background-color: powderblue;}\n</style>\n<head>\n    <meta charset="UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Resultado</title>\n</head>\n<body>\n')   
    resultado.write('    <code>\n    <h1>\n        Diretorio\n    </h1>\n        <p>\n')

    #Escrevendo o caminho do diretorio e seu tamanho
    resultado.write("            {}{}|tamanho = {} bytes|\n        </p>\n".format(caminho,("-"*(130-len(caminho))),tamanho_diretorio))

    #Escrevendo os subdiretorios e seus caminhos
    resultado.write('    <h1>\n        Subdiretorios\n    </h1>\n        <p>\n')
    for i in range(len(subdiretorios)):
        resultado.write("            {}\n            <br>\n".format(subdiretorios[i]))

    #Finalizando o html    
    resultado.write('        </p>\n    <h2>\n        Aluno: Tulio Castro Silva\n    </code>\n    </h2>\n</body>\n</html>')
    resultado.close()
    
    
if __name__ == "__main__":
    tamanho('C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_3')