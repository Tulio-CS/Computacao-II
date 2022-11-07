from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
from window import *
from window_2 import *


class app(Tk):
    def __init__(self,master=None):
        master.geometry('300x300')
        master.title("Sys")
        master.configure(bg="#3F3F3F")
        master.resizable(width=False, height=False)
        self.frame = Frame(master)
        self.clientes = Listbox(self.frame)
        self.clientes.bind("<<ListboxSelect>>",self.alterar_cliente)
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.config(command = self.clientes.yview)
        self.atualiza_lista()
        self.clientes.pack(side=LEFT)
        self.scrollbar.pack(side=RIGHT)
        self.frame.place(x=80,y=5)
        self.novo_cliente = Button(master,text="Novo cliente",width=10)
        self.novo_cliente.bind("<Button-1>",self.adicionar_cliente)
        self.novo_cliente.place(x=70,y=180)
        self.atualizar = Button(master,text="Atualizar lista",width=10)
        self.atualizar.bind("<Button-1>",self.atualizar_contato)
        self.atualizar.place(x=155,y=180)

    
    def atualiza_lista(self):
        arq = open("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_6/q4/clientes.txt","r")
        i = 1
        for linha in arq.readlines():
            linha = linha.strip("\n")
            linha = linha.split("|")
            self.clientes.insert(i,linha[0])
            i += 1
        arq.close()


    def adicionar_cliente(self,event):
        win = window(self)
        win.grab_set()
        
    
    
    def atualizar_contato(self,event):
        self.clientes.delete(0,END)
        self.atualiza_lista()

    def alterar_cliente(self,event):
        estados_civis = ["Solteiro","Casado","Separado","Divorciado","Viuvo"]
        index = self.clientes.curselection()
        arq = open("C:/Users/tulio/OneDrive/Documentos/GitHub/Computacao-II/semana_6/q4/clientes.txt","r")
        linha = arq.readlines()
        dados = linha[int(index[0])]
        dados = dados.split("|")
        win = window_2(self)
        win.title("{}".format(dados[0]))
        win.nome_entry["text"] = dados[0]
        win.cpf_entry["text"] = dados[1]
        win.estado_civil_entry["text"] = dados[2]
        win.telefone_entry["text"] = dados[3]
        win.grab_set()


if __name__ == "__main__":
    root = Tk()
    app(root)
    root.mainloop()