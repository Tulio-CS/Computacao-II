#Aluno: Tulio Castro Silva

class relogio:
    def __init__(self, hora, minuto, segundo):
        """Iniciando um objeto da classe relogio
        analisa se o relogio inserido e valido
        int, int, int -> obj"""
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
        """Definindo o metodo __add__ que soma um objeto relogio com outro
        realiza uma serie de calculos para acertar os minutos segundos e horas
        obj, obj -> obj"""
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
        """Definindo o metodo __sub__ que subtrai um objeto relogio com outro
        se o primeiro relogio for maior do que o segundo.
        (o enunciado da questao diz que o primeiro relogio precisa ser maior que o 
        segundo, nesta função isto e tratado com a estrutura condicional if
        se removida o programa calcula normalmente a hora da subtraçao de dois relogios
        o primeiro relogio nao precisa ser maior do que o segundo)
        obj, obj -> obj"""
        if self.hora < outro.hora or self.hora == outro.hora and self.minuto < outro.minuto or self.hora == outro.hora and self.minuto == outro.minuto and self.segundo < outro.segundo:
            return print("O primeiro horario deve ser maior ou igual ao segundo")
        else:
            hora = 24 + (self.hora - outro.hora)
            minuto = 60 + (self.minuto - outro.minuto)
            segundo = 60 + (self.segundo - outro.segundo)
            if (self.segundo - outro.segundo) <= 0:
                minuto -= 1
            if (minuto - self.minuto - outro.minuto) < 0:
                hora -= 1
            return relogio(hora % 24 ,minuto % 60,segundo %60)
    
    def __gt__(self,outro):
        """Definindo o metodo __gt__ que analisa se um relogio e maior do que o outro
        e retorna um valor boolenao       
        obj, obj -> bool"""
        if self.hora > outro.hora:
            return True
        elif self. hora == outro.hora and self.minuto > outro.minuto:
            return True
        elif self. hora == outro.hora and self.minuto == outro.minuto and self.segundo > outro.segundo:
            return True
        return False
    
    def __lt__(self,outro):
        """Definindo o metodo __lt__ que analisa se um relogio e menor do que outro
        obj, obj -> bool"""
        if self.hora < outro.hora:
            return True
        elif self.hora == outro.hora and self.minuto < outro.minuto:
            return True
        elif self.hora == outro.hora and self.minuto == outro.minuto and self.segundo < outro.segundo:
            return True
        return False

    def __eq__(self,outro):
        """Definindo o metodo que analisa se um relogio e igual a outro
        obj, obj -> bool"""
        if self.hora == outro.hora and self.minuto == outro.minuto and self.segundo == outro.segundo:
            return True
        return False
    
    def __str__ (self):
        """Definindo o metodo __str__ que representa o objeto no formato string
        obj -> str"""
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
    
    



