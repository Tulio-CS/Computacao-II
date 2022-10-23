#Aluno: Tulio Castro Silva

def intersecao(lista1, lista2):
    """Retorna uma lista com a intersecao da lista 1 com a lista 2
    list, list -> list"""
    return list(set(lista1).intersection(lista2))

def comparar(l1,l2):
    """retorna uma string dizendo se alguma lista e subconjunto
    list, list -> str"""
    if intersecao(l1,l2) == l1 or intersecao(l1,l2) == l2:
        if l1 == l2:
            return "As listas sao iguais"
        if l1 > l2:
            return "Lista 2 e subconjunto da lista 1"
        else:
            return "Lista 1 e subconjunto da lista 2"
    else:
        print(intersecao(l1,l2))
        return "Nao ha subconjuntos"

if __name__ == "__main__":
    l1 = [1,6,2,3,5,4]
    l2 = [1,2,3,4]
    print(comparar(l1,l2))