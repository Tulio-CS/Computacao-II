# Aluno: Túlio Castro Silva

import numpy as np


def main() -> list:
    """Funcao que resolve o sistema
    x + 10y -12z = 120
    4x -2y -20z = 60
    -x + y + 5z = 10"""
    a = np.array([[1,10,-12],[4,-2,-20],[-1,1,5]])
    b = np.array([120,60,10])

    return np.linalg.solve(a,b)

if __name__ == "__main__":
    print(main())

