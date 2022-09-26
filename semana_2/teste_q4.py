#Aluno: Tulio Castro Silva

from q4 import *

"""
    Comentarios:
    Se removido a estrutura condicional if do metodo __sub__
    o programa calculara a hora normalmente 
    (o primeiro horario não precisa ser maior do que o segundo), 
    foi adicionado esta estrutura condicional para 
    adequar as especificaçoes da questao
"""

if __name__ == "__main__":
    r0 = relogio(16,61,54)
    r1 = relogio(18,37,32)
    r2 = relogio(20,0,30)
    print(r1)
    print(r2)
    r3 = r1 + r2
    print(r3)
    r4 = r3 - r2
    print(r4)
    r4 = r2 - r3
    print(r4)
    print(r1 == r2)
    print(r1 == relogio(18,37,32))
    print(r3 > r3)
    print(r3 > r2)
    print(r2 > r3)