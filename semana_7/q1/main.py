# Aluno: Túlio Castro Silva

import numpy as np
from random import randint

def questao() -> list:
    """Funcao que gera 3 arrays com 5 valores aleatorios e soma as duas primeiras e subtrai a terceira"""
    a = np.array([randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)])
    b = np.array([randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)])
    c = np.array([randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)])

    return a + b - c

if __name__ == "__main__":
    print(questao())