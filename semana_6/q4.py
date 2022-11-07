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
        win = window(self)
        win.title("{}".format(dados[0]))
        win.adicionar_cliente["text"] = "Atualizar"
        win.nome_entry.insert(0,dados[0])
        win.cpf_entry.insert(0,dados[1])
        win.telefone_entry.insert(0,dados[3])
        win.estado_civil_entry.current(estados_civis.index(dados[2]))
        win.grab_set()



root = Tk()

app(root)
root.mainloop()