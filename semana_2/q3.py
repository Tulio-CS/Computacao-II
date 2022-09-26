#ALuno: Tulio Castro Silva

class ponto:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def __add__(self,outro):
        x = self.x + outro.x
        y = self.y + outro.y
        return ponto(x , y)
    
    def __sub__(self,outro):
        x = self.x - outro.x
        y = self.y - outro.y
        return ponto(x , y)
    
    def __mul__(self,outro):
        x = self.x * outro.x
        y = self.y * outro.y
        return ponto(x , y)
    
    def __rmul__(self,outro):
        x = self.x * outro
        y = self.y * outro
        return ponto(x , y)
         
    def __str__(self):
        return ("{} , {}".format(self.x,self.y))




