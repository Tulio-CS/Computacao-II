#Aluno: Tulio Castro Silva

from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
from window import *
from exibir import *

try:
    file = open("clientes.txt","r")
    file.close()
except FileNotFoundError:
    file = open("clientes.txt","w")
    file.close()


class app(Tk):
    def __init__(self,master=None):
        master.geometry('300x300')
        master.title("Sys")
        master.configure(bg="#3F3F3F")
        master.resizable(width=False, height=False)
        self.frame = Frame(master)
        self.clientes = Listbox(self.frame)
        self.clientes.bind("<<ListboxSelect>>",self.exibir)
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.config(command = self.clientes.yview)
        self.atualiza_lista(event=None)
        self.clientes.pack(side=LEFT)
        self.scrollbar.pack(side=RIGHT)
        self.frame.place(x=80,y=5)
        self.novo_cliente = Button(master,text="Novo cliente",width=10)
        self.novo_cliente.bind("<Button-1>",self.adicionar_cliente)
        self.novo_cliente.place(x=70,y=180)
        self.atualizar = Button(master,text="Atualizar lista",width=10)
        self.atualizar.bind("<Button-1>",self.atualiza_lista)
        self.atualizar.place(x=155,y=180)

    
    def atualiza_lista(self,event):
        self.clientes.delete(0,END)
        with open("clientes.txt","r") as f:
            reader = csv.reader(f)
            data = list(reader)
            i = 0
            for row in data:
                self.clientes.insert(i,row[0])
                i += 1
            f.close()


    def adicionar_cliente(self,event):
        win = window("","","Solteiro","","NEW")
        win.grab_set()

    def exibir (self,event):
        try:
            index = self.clientes.curselection()[0]
            with open("clientes.txt","r") as f:
                reader = csv.reader(f)
                data = list(reader)
            win = exibir(data[index][0],data[index][1],data[index][2],data[index][3],index)
            f.close()
        except IndexError:
            pass
    

    def alterar_cliente(self):
        index = self.clientes.curselection()[0]
        with open("clientes.txt","r") as f:
            reader = csv.reader(f)
            data = list(reader)
        win = window(data[index][0],data[index][1],data[index][2],data[index][3],index)
        win.grab_set()
        f.close()


if __name__ == "__main__":
    root = Tk()
    app(root)
    root.mainloop()