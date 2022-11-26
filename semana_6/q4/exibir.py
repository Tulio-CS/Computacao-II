#Aluno: Tulio Castro Silva

from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
from window import *

class exibir(Toplevel):
    def __init__(self,nome,cpf,estado_civil,telefone,index):
        Toplevel.__init__(self)
        self.geometry('230x150')
        self.title("Sys")
        self.configure(bg="#3F3F3F")
        self.resizable(width=False, height=False)
        self.nome = Label(self,text="Nome:",bg="#3F3F3F",fg="white")
        self.nome_entry = Label(self,text=nome,bg="#3F3F3F",fg="white")
        self.nome.grid(row=0,column=0,pady=2,padx=2)
        self.nome_entry.grid(row=0,column=1,pady=2,padx=2)
        self.cpf = Label(self,text="CPF:",bg="#3F3F3F",fg="white")
        self.cpf_entry = Label(self,text=cpf,bg="#3F3F3F",fg="white")
        self.cpf.grid(row=1,column=0,pady=2,padx=2)
        self.cpf_entry.grid(row=1,column=1,pady=2,padx=2)
        self.estado_civil = Label(self,text="Estado civil:",bg="#3F3F3F",fg="white")
        self.estado_civil_entry = Label(self,text=estado_civil,bg="#3F3F3F",fg="white")
        self.estado_civil.grid(row=2,column=0,pady=2,padx=2)
        self.estado_civil_entry.grid(row=2,column=1,pady=2,padx=2)
        self.telefone = Label(self,text="Telefone:",bg="#3F3F3F",fg="white")
        self.telefone_entry = Label(self,text=telefone,bg="#3F3F3F",fg="white")
        self.telefone.grid(row=3,column=0,pady=2,padx=2)
        self.telefone_entry.grid(row=3,column=1,pady=2,padx=2)
        self.adicionar_cliente = Button(self,text="Alterar",command= lambda: self.alterar(nome,cpf,estado_civil,telefone,index),width=10)
        self.adicionar_cliente.place(x=40,y=110)
        self.calcelar_botao = Button(self,text="Sair",command=self.sair,width=10)
        self.calcelar_botao.place(x=125,y=110)
    
    def alterar(self,nome,cpf,estado_civil,telefone,index):
        win = window(nome,cpf,estado_civil,telefone,index)
        win.grab_set()
        self.sair()
        
    def sair(self):
        self.destroy()




