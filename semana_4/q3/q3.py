# Aluno: Tulio Castro Silva

class Triangulo:
    def __init__(self,a,b,c):
        lados = [a,b,c]
        if self.__validade(lados):
            self.__lado_a = a
            self.__lado_b = b
            self.__lado_c = c
        else:
            raise ValueError("Lados invalidos")

    @property

    def lado_a(self):
        """Property lado A"""
        return self.__lado_a
    
    @lado_a.setter

    def lado_a(self,outro):
        """Property setter do lado A checa se o valor inserido e valido"""
        if self.__validade([outro,self.lado_b,self.lado_c]):
            self.__lado_a = outro
        else:
            raise ValueError("Lado A invalido")
        
    @property

    def lado_b(self):
        """Property lado B"""
        return self.__lado_b
    
    @lado_b.setter

    def lado_b(self,outro):
        """Property setter do lado B checa se o valor inserido e valido"""
        if self.__validade([self.lado_a,outro,self.lado_c]):
            self.__lado_b = outro
        else:
            raise ValueError("Lado B invalido")

    @property

    def lado_c(self):
        """Property lado C"""
        return self.__lado_c
    
    @lado_c.setter

    def lado_c(self,outro):
        """Property setter do lado C checa se o valor inserido e valido"""
        if self.__validade([self.lado_a,self.lado_b,outro]):
            self.__lado_c = outro
        else:
            raise ValueError("Lado C invalido")
       
    def __validade(self,lados):
        """Diz se o triangulo e valido de acordo com o tamanho de seus lados"""
        if max(lados) >= (sum(lados)-max(lados)):
            return False
        else:
            return True
    
    def __str__ (self):
        return ("A:{}\nB:{}\nC:{}".format(self.lado_a,self.lado_b,self.lado_c))

if __name__ == "__main__":
    t1 = Triangulo(3,4,5)
    print(t1)
    t1.lado_c = 6
    print(t1)
    t2 = Triangulo(3,4,6)
    t2.lado_c = 7
    print(t2)