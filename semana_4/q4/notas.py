class notas:
    def __init__(self,nota1, nota2, nota3):
        if nota1 < 0 or nota2 < 0 or nota3 < 0:
            raise("Nota invalida")
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3
    
    @property
    def nota1(self):
        return self.__nota1
    
    @nota1.setter
    def nota1(self,valor):
        if valor < 0 or valor >10:
            raise("Valor invalido")
        self.__nota1 = valor

    @property
    def nota2(self):
        return self.__nota2
    
    @nota2.setter
    def nota2(self,valor):
        if valor < 0 or valor >10:
            raise("Valor invalido")
        self.__nota2 = valor

    @property
    def nota3(self):
        return self.__nota3
    
    @nota3.setter
    def nota3(self,valor):
        if valor < 0 or valor >10:
            raise("Valor invalido")
        self.__nota3 = valor

    
    def calculaMedia(self):
        return (self.nota1 + self.nota2 + self.nota3)/3