# Aluno: Túlio Castro Silva

import csv 
import numpy as np
import matplotlib.pyplot as plt


def main(path:str) -> None:
    """Funcao que plota uma espiral dado arquivo .csv"""

    one = [[],[]]
    two = [[],[]]
    three = [[],[]]

    # Abrindo os arquivos
    with open(path,"r") as file:

        reader = csv.reader(file)
        data = list(reader)
        
        # Obtendo os pontos
        for i in range(len(data)):

            if data[i][2] == "1":
                one[0].append(float(data[i][0]))
                one[1].append(float(data[i][1]))

            if data[i][2] == "2":
                two[0].append(float(data[i][0]))
                two[1].append(float(data[i][1]))

            if data[i][2] == "3":
                three[0].append(float(data[i][0]))
                three[1].append(float(data[i][1]))
        file.close()

    # Plotando
    plt.plot(one[0],one[1],"oy",markersize=0.9)
    plt.plot(two[0],two[1],"oc",markersize=0.9)
    plt.plot(three[0],three[1],"om",markersize=0.9)
    plt.show()

if __name__ == "__main__":
    main("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_7/q5/spiral.csv")