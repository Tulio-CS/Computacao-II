# Aluno: Túlio Castro Silva

from random import randint
import numpy as np

def main(n:int) -> list:
    """Funcao que cria uma arrayu NxN contendo valores aleatorios entre
    5 e 50"""
    array = np.zeros(shape=(n,n))

    for i in range(0,n):
        for j in range(0,n):
            array[i][j] = randint(5,50)

    return array
if __name__ == "__main__":
    print(main(10))