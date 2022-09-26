#Aluno: Tulio Castro Silva

from q1 import *

if __name__ == "__main__":
    ret = retangulo(2,3)
    print(ret.area())
    print(ret.perimetro())

    cai = caixa(2,2,2)
    print(cai.volume())
    print(cai.area())

    cir = circulo(3)
    print(cir.area())
    print(cir.perimetro())

    cil = cilindro(3,4)
    print(cil.volume())
    print(cil.area())