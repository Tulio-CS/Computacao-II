#Aluno: Tulio Castro Silva

from tkinter import * 
from math import sqrt

class janela:
    def __init__(self,master= None):
        #Titulo
        self.titulo = Frame(master)
        self.titulolabel = Label(self.titulo,text='CALCULADORA DE IMC')
        self.titulolabel.pack(side=LEFT)
        self.titulo.place(x=30,y=0)
        #Altura
        self.container_altura = Frame(master)
        self.altura = Label(self.container_altura,text="Altura(m):")
        self.val_altura = Entry(self.container_altura,width=22)
        self.altura.pack(side=LEFT)
        self.val_altura.pack(side=RIGHT)
        self.container_altura.place(x=0,y=30)
        #Peso
        self.container_peso = Frame(master)
        self.peso = Label(self.container_peso,text="Peso(Kg):")
        self.val_peso = Entry(self.container_peso,width=23)
        self.peso.pack(side=LEFT)
        self.val_peso.pack(side=RIGHT)
        self.container_peso.place(x=0,y=55)
        #Resultado
        self.container_resultado = Frame(master)
        self.resultado = Label(self.container_resultado,text="Resultado:")
        self.val_resultado = Entry(self.container_resultado,width=22)
        self.resultado.pack(side=LEFT)
        self.val_resultado.pack(side=RIGHT)
        self.container_resultado.place(x=0,y=80)
        #Classificacao
        self.container_classificacao = Frame(master)
        self.classificacao = Label(self.container_classificacao,text="Classificacao :")
        self.val_classificacao = Label(self.container_classificacao,text="")
        self.classificacao.pack(side=LEFT)
        self.val_classificacao.pack(side=RIGHT)
        self.container_classificacao.place(x=0,y=105)
        #Botoes
        self.buttons_container = Frame(master)
        self.calcular = Button(self.buttons_container,text="Calcular")
        self.calcular.pack(side=LEFT)
        self.limpar = Button(self.buttons_container,text="Limpar")
        self.limpar.pack(side=RIGHT)
        self.buttons_container.place(x=50,y=130)
        self.calcular.bind("<Button-1>",self.calcula_imc)
        self.limpar.bind("<Button-1>",self.limpar_resultado)

    def calcula_imc(self,event):
        if len(self.val_peso.get()) != 0 and len(self.val_resultado.get()) != 0 and len(self.val_altura.get()) != 0:
            self.val_resultado.delete(0,"end")
        if len(self.val_resultado.get()) == 0:
            imc = float(self.val_peso.get())/(float(self.val_altura.get())**2)
            self.val_resultado.delete(0,"end")
            self.val_resultado.insert(0,round(imc,2))
        if len(self.val_altura.get()) == 0:
            altura = sqrt(float(self.val_peso.get())/float(self.val_resultado.get()))
            self.val_altura.delete(0,"end")
            self.val_altura.insert(0,round(altura,2))
            imc = float(self.val_peso.get())/(float(self.val_altura.get())**2)
        if len(self.val_peso.get()) == 0:
            peso = float(self.val_resultado.get()) * (float(self.val_altura.get())**2)
            self.val_peso.delete(0,"end")
            self.val_peso.insert(0,round(peso,2))
            imc = float(self.val_peso.get())/(float(self.val_altura.get())**2)
        if imc > 40:
             self.val_classificacao["text"] = ("Obesidade (grau III)")
        elif imc > 35:
            self.val_classificacao["text"] = ("Obesidade (grau II)")
        elif imc > 30:
            self.val_classificacao["text"] = ("Obesidade (grau I)")
        elif imc > 25:
            self.val_classificacao["text"] = ("Excesso de peso")
        elif imc > 18.5:
            self.val_classificacao["text"] = ("Peso normal")
        else:
            self.val_classificacao["text"] = ("Abaixo do peso ideal")
        return 0

    def limpar_resultado(self,event):
        self.val_peso.delete(0,"end")
        self.val_altura.delete(0,"end")
        self.val_resultado.delete(0,"end")
        self.val_classificacao["text"] = ""

root = Tk()
root.geometry("200x160")
root.resizable(width=False, height=False)
root.title("IMC")
janela(root)

root.mainloop()