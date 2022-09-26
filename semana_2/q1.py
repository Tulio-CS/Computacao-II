#Aluno: Tulio Castro Silva

from math import pi

class retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (2 * self.base) + (2 * self.altura)

class caixa(retangulo):
    def __init__(self,base_1 , base_2, altura):
        super().__init__(base_1,base_2)
        self.altura2 = altura
    
    def volume(self):
        return super().area() * self.altura2
    
    def area(self):
        return 2 * ((self.base * self.altura) + (self.base * self.altura2) + (self.altura * self.altura2))

class circulo:
    def __init__(self,raio):
        self.raio = raio

    def area(self):
        return pi * (self.raio ** 2)
    
    def perimetro(self):
        return 2 * pi * self.raio

class cilindro(circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura
    
    def volume(self):
        return super().area() * self.altura
    
    def area(self):
        return (2 * super().area()) + (2 * super().perimetro() * self.altura)



