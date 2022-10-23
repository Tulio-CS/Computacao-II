# Aluno: Tulio Castro Silva

class pessoa:
    def __init__(self, identidade, cpf, nome= "", telefone= "", endereco = "", idade = 0):
        if len(str(identidade)) > 9:
            raise ValueError("Identidade invalida")
        if len(str(cpf)) > 11:
            raise ValueError("CPF invalido")
        if idade < 0:
            raise ValueError("Idade invalida")            
        self.identidade = identidade
        self.cpf = cpf
        self.nome = nome 
        self.telefone = telefone
        self.endereco = endereco
        self.idade = idade
    
