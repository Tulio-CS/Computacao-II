#Aluno: Tulio Castro Silva

def main(convidados,x,y):
    """funcao que retorna a diferenca entre a lista de convidados, a lista x e a lista y
    list, list, list -> list"""
    nao_comeram = list(set(convidados).difference(x).difference(y))
    return nao_comeram

if __name__ == "__main__":
    conv = ["tulio","tiago","reginaldo","paulo","tania","iomar","bernardo"]
    x = ["tiago","paulo","bernardo","reginaldo"]
    y = ["paulo","tania","iomar"]
    print(main(conv,x,y))