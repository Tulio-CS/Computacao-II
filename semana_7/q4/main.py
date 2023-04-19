# Aluno: Túlio Castro Silva

import matplotlib.pyplot as plt
import numpy as np
from math import factorial,pi

def main() -> None:
    """Funcao que plota a funcao seno e os primeiros polinomios de taylor"""

    x = np.linspace(-pi,pi,100) # Limites do grafico
    y = np.sin(x) # Funcao seno
    plt.plot(x,y,"#F4D03F",label="seno")

    one = [] # Polinomio numero 1
    two = [] # Polinomio numero 2 
    three = [] # Polinomio numero 3
    four = [] # Polinomio numero 4

    # Calculando os pontos dos polinomios
    for i in range(len(x)):

        one.append(polinomio_1(x[i])) 
        two.append(polinomio_2(x[i]))
        three.append(polinomio_3(x[i]))
        four.append(polinomio_4(x[i]))

    # Plotando os polinomios de Taylor
    plt.title("Grafico da função seno e dos primeiros polinomios de Taylor")
    plt.plot(x,one,"#C0392B",label="polinomio 1")
    plt.plot(x,two,"#229954",label="polinomio 3")
    plt.plot(x,three,"#5499C7",label="polinomio 5")
    plt.plot(x,four,"pink",label="polinomio 7")
    plt.legend()
    plt.show()

def polinomio_1(x):
    return x

def polinomio_2(x):
    return polinomio_1(x) - (x*x*x)/factorial(3)

def polinomio_3(x):
    return polinomio_2(x) + (x*x*x*x*x)/factorial(5)

def polinomio_4(x):
    return polinomio_3(x) - (x*x*x*x*x*x*x)/factorial(7)

if __name__ == "__main__":
    main()
