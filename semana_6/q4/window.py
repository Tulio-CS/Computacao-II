from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *

class window(Toplevel):
    def __init__(self,master):
        Toplevel.__init__(self)
        self.geometry('230x150')
        self.title("Sys")
        self.configure(bg="#3F3F3F")
        self.resizable(width=False, height=False)
        self.nome = Label(self,text="Nome:",bg="#3F3F3F",fg="white")
        self.nome_entry = Entry(self)
        self.nome.grid(row=0,column=0,pady=2,padx=2)
        self.nome_entry.grid(row=0,column=1,pady=2,padx=2)
        self.nome = Label(self,text="Nome:",bg="#3F3F3F",fg="white")
        self.nome_entry = Entry(self)
        self.nome.grid(row=0,column=0,pady=2,padx=2)
        self.nome_entry.grid(row=0,column=1,pady=2,padx=2)
        self.cpf = Label(self,text="CPF:",bg="#3F3F3F",fg="white")
        self.cpf_entry = Entry(self)
        self.cpf.grid(row=1,column=0,pady=2,padx=2)
        self.cpf_entry.grid(row=1,column=1,pady=2,padx=2)
        self.estado_civil = Label(self,text="Estado civil:",bg="#3F3F3F",fg="white")
        self.estado_civil_entry = ttk.Combobox(self,width=17,state="readonly")
        self.estado_civil_entry["values"] = ["Solteiro","Casado","Separado","Divorciado","Viuvo"]
        self.estado_civil_entry.current(0)
        self.estado_civil.grid(row=2,column=0,pady=2,padx=2)
        self.estado_civil_entry.grid(row=2,column=1,pady=2,padx=2)
        self.telefone = Label(self,text="Telefone:",bg="#3F3F3F",fg="white")
        self.telefone_entry = Entry(self)
        self.telefone.grid(row=3,column=0,pady=2,padx=2)
        self.telefone_entry.grid(row=3,column=1,pady=2,padx=2)
        self.adicionar_cliente = Button(self,text="Adicionar",command=self.adicionar,width=10)
        self.adicionar_cliente.place(x=40,y=110)
        self.calcelar_botao = Button(self,text="Cancelar",command=self.cancela,width=10)
        self.calcelar_botao.place(x=125,y=110)
    
    def adicionar(self):
        self.valida()
    
    def cancela(self):
        self.destroy()
    
    def valida(self):
        if len(self.nome_entry.get()) == 0:
            showerror("ERRO","Nome invalido")
        elif len(self.cpf_entry.get()) != 11:
            showerror("ERRO","CPF invalido")
        elif len(self.telefone_entry.get()) == 0:
            showerror("ERRO","Telefone invalido")
        else:
            arq = open("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_6/q4/clientes.txt","a")
            arq.write("{}|{}|{}|{}\n".format(self.nome_entry.get(),self.cpf_entry.get(),self.estado_civil_entry.get(),self.telefone_entry.get()))
            arq.close()
            self.destroy()
