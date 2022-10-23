# Aluno: Tulio Castro Silva


def nomes():
    lista = []
    while True:
        x = input("Digite um nome:")
        if x == "":
            break
        elif x in lista:
            continue
        else:
            lista.append(x)
    for i in range(len(lista)):
        print(lista[i].split(" ",1)[0])

if __name__ == "__main__":
    nomes()

