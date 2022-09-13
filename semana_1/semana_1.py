# Autor: Túlio Castro Silva

# Questão 1

class Veiculo:

    def __init__(self,cons_comb,cap_comb):
        """Metodo construtor da classe veiculo"""
        self.cons_comb = cons_comb
        self.cap_comb = cap_comb
        self.qtd_comb = 0.0
    
    def mover(self,km):
        """funcao que verifica se o automovel possui combustivel para locomover determinada kilometragem
        em caso afirmativo ela anda com o veiculo e diminui sua quantidade de combustivel"""
        if (self.qtd_comb * self.cons_comb) >= km:
            self.qtd_comb -= (km * self.cons_comb)
            print("o veiculo andou {}".format(km))
        else:
            print("Não ha combustivel suficiente")

    def getCombustivel(self):
        """Funcao que retorna a quantidade de combustivel do veiculo"""
        return self.qtd_comb

    def abastecer(self,litros):
        """Funcao que aumenta a quantidade de combustivel do veiculo, sem deixar ultrapassar a quantidade maxima"""
        if litros > 0 :
            if self.qtd_comb + litros <= self.cap_comb:
                self.qtd_comb += litros
            else:
                print("Não é possivel abastecer essa quantidade de combustivel no veiculo")
        else:
            print("A quantidade desejada não e valida")

def main_veiculo():
    carro = Veiculo(10,101)
    carro.abastecer(-1)
    print(carro.getCombustivel())
    carro.abastecer(100)
    print(carro.getCombustivel())
    carro.mover(10)
    print(carro.getCombustivel())

################################################################################################################################

# Questão 2

class Funcionario():
    def __init__(self,nome,departamento,salario,data_entrada,cpf,ativo):
        self.nome = nome
        self.departamento = departamento
        self.salario = salario
        self.data_entrada = data_entrada
        self.cpf = cpf
        self.ativo = ativo
    
    def bonificar(self,valor):
        """Funcao que aumenta o salario de determinado funcionario caso este esteja ativo na empresa"""
        if self.ativo == True:
            self.salario += valor
        else:
            print("Esse funcionario ja foi demitido")
        
    def demitir (self):
        """Funcao que demite determinado funcionario"""
        if self.ativo == True:
            self.ativo = not(self.ativo)
        else:
            print("Esse funcionario ja foi demitido") 

def main_funcionario():
    jorge = Funcionario("Jorge","ri",100,"25/12/2004","10677777710",True)

    jorge.bonificar(101)
    print(jorge.salario)
    print(jorge.ativo)
    jorge.demitir()
    jorge.bonificar(102)
    print(jorge.ativo)

################################################################################################################################

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
    
    def calculaPerimetro(self):
        """Retorna o perimetro de um determinado objeto triangulo"""
        return (self.lado_a + self.lado_b + self.lado_c)

    def calculaArea(self):
        """Calcula a area do triangulo pela formula de heron"""
        p = self.lado_a + self.lado_b + self.lado_c
        return sqrt(p*(p-self.lado_a)*(p-self.lado_b)*(p-self.lado_c))

def main_triangulo():
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
    print(equilatero.calculaPerimetro())
    print(isoceles.calculaPerimetro())
    print(escaleno.calculaPerimetro())
    print("\n")
    print(equilatero.calculaArea())
    print(isoceles.calculaArea())
    print(escaleno.calculaArea())

################################################################################################################################

# Questão 4

from math import sqrt

class Ponto2D():
    def __init__(self,x,y):
        """Funçao que cria um ponto em um plano dado seus pontos x e y"""
        self.x = x
        self.y = y
    
    def distancia(self,ponto):
        """retorna a distancia entre dois pontos"""
        d = ((self.x - ponto.x)**2) + ((self.y + ponto.y)**2)
        if d < 0:
            return sqrt(-d)
        return sqrt(d) 

def main_pontos():   
    ponto1 = Ponto2D(7,8)
    ponto2 = Ponto2D(4,10)

    print(ponto1.distancia(ponto2))



        