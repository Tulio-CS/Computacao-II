# Aluno: Tulio Castro Silva

class notas:
    def __init__(self,nota1, nota2, nota3):
        if nota1 < 0 or nota2 < 0 or nota3 < 0:
            raise ValueError("Nota invalida")
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3
    
    @property
    def nota1(self):
        """propriedade nota 1"""
        return self.__nota1
    
    @nota1.setter
    def nota1(self,valor):
        """Nota 1 setter checa se o valor inserido e valido"""
        if valor < 0 or valor >10:
            raise ValueError("Valor invalido")
        self.__nota1 = valor

    @property
    def nota2(self):
        """propriedade nota 2"""
        return self.__nota2
    
    @nota2.setter
    def nota2(self,valor):
        """Nota 2 setter checa se o valor inserido e valido"""
        if valor < 0 or valor >10:
            raise ValueError("Valor invalido")
        self.__nota2 = valor

    @property
    def nota3(self):
        """propriedade nota 3"""
        return self.__nota3
    
    @nota3.setter
    def nota3(self,valor):
        """Nota 3 setter checa se o valor inserido e valido"""
        if valor < 0 or valor >10:
            raise ValueError("Valor invalido")
        self.__nota3 = valor

    
    def calculaMedia(self):
        """Calcula a media
        -> int"""
        return (self.nota1 + self.nota2 + self.nota3)/3