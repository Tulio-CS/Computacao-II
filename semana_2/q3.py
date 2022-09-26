#ALuno: Tulio Castro Silva

class ponto:
    def __init__(self, x, y):
        """Iniciando um objeto da classe ponto com determinadas coordenadas X e Y
        int, int -> obj"""
        self.x = x 
        self.y = y
    
    def __add__(self,outro):
        """definindo o metodo __add__ que soma dois pontos
        obj, obj -> obj"""
        x = self.x + outro.x
        y = self.y + outro.y
        return ponto(x , y)
    
    def __sub__(self,outro):
        """definindo o metodo __sub__ de subtrai dois pontos
        obj, obj -> obj"""
        x = self.x - outro.x
        y = self.y - outro.y
        return ponto(x , y)
    
    def __mul__(self,outro):
        """definindo o metodo __mul__ que multiplica dois pontos
        obj, obj -> obj"""
        x = self.x * outro.x
        y = self.y * outro.y
        return ponto(x , y)
    
    def __rmul__(self,outro):
        """definindo o metodo __rmul__ que multiplica um ponto por um numero
        obs: o numero deve estar a direita na operacao
        int, obj -> obj"""
        x = self.x * outro
        y = self.y * outro
        return ponto(x , y)
         
    def __str__(self):
        """Definindo a string que representa o objeto ponto
        obj -> str"""
        return ("{} , {}".format(self.x,self.y))




