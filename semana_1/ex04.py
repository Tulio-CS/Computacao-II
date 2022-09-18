#Aluno: Túlio Castro Silva

from math import sqrt

class Ponto2D():
    def __init__(self,x,y):
        """Funçao que cria um ponto em um plano dado seus pontos x e y"""
        self.x = x
        self.y = y
    
    def distancia(self,ponto):
        """retorna a distancia entre dois pontos"""
        d = ((self.x - ponto.x)**2) + ((self.y + ponto.y)**2)
        if d < 0:
            return sqrt(-d)
        return sqrt(d) 

if __name__ == "__main__":
    """Testando a classe criada"""
    ponto1 = Ponto2D(7,8)
    ponto2 = Ponto2D(4,10)
    print(ponto1.distancia(ponto2))