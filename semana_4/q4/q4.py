class pessoa:
    def __init__(self, identidade, cpf, nome= "", telefone= "", endereco = "", idade = 0):
        if len(str(identidade)) > 9:
            raise("Identidade invalida")
        if len(str(cpf)) > 11:
            raise("CPF invalido")
        if idade < 0:
            raise("Idade invalida")            
        self.identidade = identidade
        self.cpf = cpf
        self.nome = nome 
        self.telefone = telefone
        self.endereco = endereco
        self.idade = idade
    

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


class aluno(pessoa,notas):
    def __init__(self,identidade, cpf, matricula, nota1, nota2 , nota3, nome= "", telefone= "", endereco = "", idade = 0):
        pessoa.__init__(self, identidade, cpf, nome ,telefone,endereco, idade)
        notas.__init__(self,nota1,nota2,nota3)
        self.matricula = matricula
    
    def visualizarMedia(self):
        print(self.calculaMedia())

class professor(pessoa):
    def __init__(self, identidade, cpf, salario = 0, nome= str, telefone= str, endereco = str, idade = 0):
        pessoa.__init__(self, identidade, cpf, nome ,telefone,endereco, idade)
        if int(salario) < 0:
            raise("Salario invalido")
        self.__salario = salario
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,valor):
        if valor < 0:
            raise("Valor invalido")
        self.__salario = valor

class professorHorista(professor):
    def __init__(self, identidade, cpf, valorHora, horasTrabalhadas, nome= "", telefone= "", endereco = "", idade = 0):
        professor.__init__(self,identidade,cpf,0,nome,telefone,endereco,idade)
        # professor.__init__(self, identidade, cpf, nome, telefone, endereco , idade)        
        if valorHora < 0:
            raise("Valor da hora invalido")
        if horasTrabalhadas < 0:
            raise("Valor para horas trabalhadas invalido")
        self.__valorHora = valorHora
        self.__horasTrabalhadas = horasTrabalhadas
    
    @property
    def valorHora(self):
        return self.__valorHora
    
    @valorHora.setter
    def valorHora(self,valor):
        if valor < 0:
            raise("Valor invalido")
        self.__valorHora = valor
    
    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @horasTrabalhadas.setter
    def horasTrabalhadas(self,valor):
        if valor < 0:
            raise("Valor invalido")
        self.__horasTrabalhadas = valor
    
    def calcularSalario(self):
        valor = self.valorHora * self.horasTrabalhadas
        self.salario = valor
    

class controller:
    def __init__(self,listaAlunos = [],listaProfessores = []):
        self.listaAlunos = listaAlunos
        self.listaProfessores = listaProfessores

    def incluirAluno(self,obj):
        if type(obj) == aluno:
            self.listaAlunos.append(obj)
        else:
            raise("Tipo de entrada invalido")

    def pesquisarAlunoPorNome(self,nome):
        for i in range(len(self.listaAlunos)):
            if self.listaAlunos[i].nome == nome:
                return self.listaAlunos[i]
            else:
                continue
        return False
    
    def pesquisarAlunoPorCPF(self,cpf):
        for i in range(len(self.listaAlunos)):
            if self.listaAlunos[i].cpf == cpf:
                return self.listaAlunos[i]
            else:
                continue
        return False
    
    def incluirProfessor(self,obj):
        if type(obj) == professor or type(obj) == professorHorista:
            self.listaProfessores.append(obj)
        else:
            raise("Tipo de entrada invalida")
    
    def pesquisarProfessorPorNome(self,nome):
        for i in range(len(self.listaProfessores)):
            if self.listaProfessores[i].nome == nome:
                return self.listaProfessores[i]
            else:
                continue
        return False
    
    def pesquisarProfessorPorCPF(self,cpf):
        for i in range(len(self.listaProfessores)):
            if self.listaProfessores[i].cpf == cpf:
                return self.listaProfessores[i]
            else:
                continue
        return False




if __name__ == "__main__":
    con = controller()
    tulio = aluno("000000001","00000000001","matricula-tulio",10,8,9,nome="Tulio",telefone="Telefone Tulio",idade=18)
    vitinho = aluno("000000002","00000000002","matricula-vitinho",7,5,8,telefone="Telefone do vitinho",nome="Vitinho")
    avellar = aluno("000000003","00000000003","matricula-avellar",8,8,8,nome="Avellar")
    con.incluirAluno(tulio)
    con.incluirAluno(vitinho)
    con.incluirAluno(avellar)
    bruno = professorHorista("000000004","00000000004",10,1,nome="bruno")
    leonardo = professor("000000005","00000000005",2500,nome="leonardo")
    dennis = professor("000000006","00000000006",1500,nome="dennis")
    con.incluirProfessor(bruno)
    con.incluirProfessor(leonardo)
    con.incluirProfessor(dennis)
    (con.pesquisarAlunoPorCPF("00000000001").visualizarMedia())
    (con.pesquisarAlunoPorCPF("00000000002").visualizarMedia())
    bruno.calcularSalario()
    print(con.pesquisarProfessorPorNome("bruno").salario)
        