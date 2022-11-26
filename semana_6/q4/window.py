#Aluno: Tulio Castro Silva

from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
import csv
path = "clientes.txt"
class window(Toplevel):
    def __init__(self,nome,cpf,estado_civil,telefone,index):
        Toplevel.__init__(self)
        self.geometry('230x150')
        self.title("Sys")
        self.configure(bg="#3F3F3F")
        self.resizable(width=False, height=False)
        self.nome = Label(self,text="Nome:",bg="#3F3F3F",fg="white")
        self.nome_entry = Entry(self)
        self.nome.grid(row=0,column=0,pady=2,padx=2)
        self.nome_entry.grid(row=0,column=1,pady=2,padx=2)
        self.nome_entry.insert(0,nome)
        self.cpf = Label(self,text="CPF:",bg="#3F3F3F",fg="white")
        self.cpf_entry = Entry(self)
        self.cpf_entry.insert(0,cpf)
        self.cpf.grid(row=1,column=0,pady=2,padx=2)
        self.cpf_entry.grid(row=1,column=1,pady=2,padx=2)
        self.estado_civil = Label(self,text="Estado civil:",bg="#3F3F3F",fg="white")
        self.estado_civil_entry = ttk.Combobox(self,width=17,state="readonly")
        self.estado_civil_entry["values"] = ["Solteiro","Casado","Separado","Divorciado","Viuvo"]
        self.estado_civil_entry.current(self.estado_civil_entry["values"].index(estado_civil))
        self.estado_civil.grid(row=2,column=0,pady=2,padx=2)
        self.estado_civil_entry.grid(row=2,column=1,pady=2,padx=2)
        self.telefone = Label(self,text="Telefone:",bg="#3F3F3F",fg="white")
        self.telefone_entry = Entry(self)
        self.telefone_entry.insert(0,telefone)
        self.telefone.grid(row=3,column=0,pady=2,padx=2)
        self.telefone_entry.grid(row=3,column=1,pady=2,padx=2)
        self.salvar = Button(self,text="Salvar",command= lambda: self.add_client(index),width=10)
        self.salvar.place(x=40,y=110)
        self.calcelar_botao = Button(self,text="Cancelar",command=self.cancela,width=10)
        self.calcelar_botao.place(x=125,y=110)

    def add_client(self,index):
        self.valida(index)
    
    
    def cancela(self):
        self.destroy()
    
    def valida(self,index):
        if len(self.nome_entry.get()) == 0:
            showerror("ERRO","Nome invalido")
        elif len(self.cpf_entry.get()) != 11:
            showerror("ERRO","CPF invalido")
        elif len(self.telefone_entry.get()) == 0:
            showerror("ERRO","Telefone invalido")
        else:
            if index == "NEW":
                with open(path,"a",newline="") as fw:
                    writer = csv.writer(fw)
                    writer.writerow([self.nome_entry.get(),self.cpf_entry.get(),self.estado_civil_entry.get(),self.telefone_entry.get()])
                    fw.close()
            else:
                with open(path,"r") as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    data[index] = [self.nome_entry.get(),self.cpf_entry.get(),self.estado_civil_entry.get(),self.telefone_entry.get()]
                    with open(path,"w",newline = "") as fw:
                        writer = csv.writer(fw)
                        for row in data:
                            writer.writerow(row)
                    fw.close()
                    f.close()
            self.destroy()
