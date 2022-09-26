#Aluno: Tulio Castro Silva

from math import pi

class retangulo:
    def __init__(self,base,altura):
        """Iniciando um objeto da classe retangulo
        int, int -> obj"""
        self.base = base
        self.altura = altura
    
    def area(self):
        """Calculando a area de um retangulo dadas sua base e altura
        obj -> int"""
        return self.base * self.altura
    
    def perimetro(self):
        """Calculando o perimetro do retangulo dadas sua base e altura
        obj -> int"""
        return (2 * self.base) + (2 * self.altura)

class caixa(retangulo):
    def __init__(self,base_1 , base_2, altura):
        """Iniciando um objeto da classe caixa, derivada da classe retangulo
        int, int, int -> obj"""
        super().__init__(base_1,base_2)
        self.altura2 = altura
    
    def volume(self):
        """calcula o volume da caixa multiplicando a area do retangulo correspondente
        a caixa com sua altura
        obj -> int"""
        return super().area() * self.altura2
    
    def area(self):
        """calcula a area de uma caixa dada as suas bases e sua altura
        obj -> int"""
        return 2 * ((self.base * self.altura) + (self.base * self.altura2) + (self.altura * self.altura2))

class circulo:
    def __init__(self,raio):
        """iniciando um objeto circulo, com um determinado raio
        int -> obj"""
        self.raio = raio

    def area(self):
        """Calculando a area de um circulo a partir de seu raio
        obj -> int"""
        return pi * (self.raio ** 2)
    
    def perimetro(self):
        """Calculando o perimetro de um circulo dado o seu raio
        obj -> int"""
        return 2 * pi * self.raio

class cilindro(circulo):
    def __init__(self, raio, altura):
        """iniciando um objeto classe cilindo, derivada da classe circulo
        int, int -> obj"""
        super().__init__(raio)
        self.altura = altura
    
    def volume(self):
        """Calculando o volume de um cilindo a partir da area de seu circulo com sua altura
        obj -> int"""
        return super().area() * self.altura
    
    def area(self):
        """Calculando a area de um cilindo usando a area e perimetro de seu circulo
        e multiplicando por sua altura
        obj -> int"""
        return (2 * super().area()) + (2 * super().perimetro() * self.altura)



