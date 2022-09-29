arquivo = open('numeros.txt','w')

for linha in range(1,21):
    arquivo.write(str(linha) + "\n")
arquivo.close()