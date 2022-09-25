class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    @property

    def raio(self):
        print("Get raio")
        return self.__raio

    @raio.setter

    def raio(self, value):
        print("Set raio")
        self.__raio= value

    @raio.deleter

    def raio(self):
        print("Delete raio")
        del self.__raio

c = Circulo(10)
c.raio = 100
print(c.raio)