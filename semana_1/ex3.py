from math import sqrt

class Triangulo():
    def __init__(self,a,b,c):
        self.lado_a = a
        self.lado_b = b
        self.lado_c = c
    
    def ehValido(self):
        """Diz se o triangulo e valido de acordo com o tamanho de seus lados"""
        lados = [self.lado_a,self.lado_b,self.lado_c]
        if min(lados) < (sum(lados)-min(lados)):
            print("E valido")
        else:
            print("Nao e valido")
    
    def TipoTriangulo(self):
        """Diz o tipo de triangulo de acordo com o tamanho de seus lados"""
        if self.lado_a == self.lado_b == self.lado_c:
            print("É equilatero")
        elif self.lado_a == self.lado_b or self.lado_a == self.lado_c or self.lado_b == self.lado_c:
            print("É isoceles")
        else:
            print("É escaleno")

    def calculaArea(self):
        """Calcula a area do triangulo pela formula de heron"""
        p = self.lado_a + self.lado_b + self.lado_c
        return sqrt(p*(p-self.lado_a)*(p-self.lado_b)*(p-self.lado_c))

equilatero = Triangulo(3,3,3)
isoceles = Triangulo(3,3,2)
escaleno = Triangulo(3,4,5)

escaleno.ehValido()
isoceles.ehValido()
escaleno.ehValido()
print("\n")
equilatero.TipoTriangulo()
isoceles.TipoTriangulo()
escaleno.TipoTriangulo()
print("\n")
print(equilatero.calculaArea())
print(isoceles.calculaArea())
print(escaleno.calculaArea())

