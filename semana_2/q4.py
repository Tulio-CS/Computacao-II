#Aluno: Tulio Castro Silva

class relogio:
    def __init__(self, hora, minuto, segundo):
        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 60:
            print("Horario digitado invalido")
            self.hora = 0
            self.minuto = 0
            self.segundo = 0
        else:
            self.hora = hora
            self.minuto = minuto
            self.segundo = segundo
    
    def __add__(self,outro):
        hora = 0
        minuto = 0
        segundo = 0
        if (self.segundo + outro.segundo) >= 60:
            minuto += 1
        if (minuto + self.minuto + outro.minuto) >= 60:
            hora += 1
        hora += (self.hora + outro.hora)
        minuto += (self.minuto + outro.minuto)
        segundo += (self.segundo + outro.segundo)
        return relogio(hora % 24 ,minuto % 60,segundo %60)
    
    def __sub__(self,outro):
        hora = 0
        minuto = 0
        segundo = 0
        if (self.hora - outro.hora) <= 0:
            hora -= 1
        if (self.minuto - outro.minuto) <= 0:
            minuto -= 1
        if (self.segundo - outro.segundo) == 0:
            segundo = 59
        hora += (self.hora - outro.hora)
        minuto += (self.minuto - outro.minuto)
        segundo += (self.segundo - outro.segundo)
        return relogio(hora % 24 ,minuto % 60,segundo %60)
    
    def __gt__(self,outro):
        if self.hora > outro.hora:
            return True
        elif self.minuto > outro.minuto:
            return True
        elif self.segundo > outro.segundo:
            return True
        return False
    
    def __lt__(self,outro):
        if self.hora < outro.hora:
            return True
        elif self.minuto < outro.minuto:
            return True
        elif self.segundo < outro.segundo:
            return True
        return False

    def __eq__(self,outro):
        if self.hora == outro.hora and self.minuto == outro.minuto and self.segundo == outro.segundo:
            return True
        return False
    
    def __str__ (self):
        hora = self.hora
        minuto = self.minuto
        segundo = self.segundo
        if self.hora < 10:
            hora = "0{}".format(self.hora)
        if self.minuto < 10:
            minuto = "0{}".format(self.minuto)
        if self.segundo < 10:
            segundo = "0{}".format(self.segundo)
        return "{} : {} : {}".format(hora,minuto,segundo)
    
    

r1 = relogio(0,0,2)
r2 = relogio(0,0,1)
r3 = r1-r2
print(r1)
print(r2)
print(r3)

