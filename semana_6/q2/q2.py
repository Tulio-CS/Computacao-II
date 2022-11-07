from tkinter import * 
from tkinter.messagebox import *

class window:
    def __init__(self,master=None):
        #variaveis
        self.tentativas = IntVar(master,name="tentativas")
        master.setvar(name="tentativas",value=0)
        #Titulo
        self.texto = Label(master,text="Insira seus dados")
        self.texto.place(x=60,y=10)
        #Usuario
        self.usuariolabel = Label(master,text="Usúario:")
        self.usuariolabel.place(x=100,y=30)
        self.val_usuario = Entry(master,width=35)
        self.val_usuario.place(x=150,y=30)
        #Senha
        self.senhalabel = Label(master,text="Senha:")
        self.senhalabel.place(x=100,y=55)
        self.val_senha = Entry(master,show="*",width=35)
        self.val_senha.place(x=150,y=55)
        #Botoes
        self.botaologin = Button(master,text="Login",bg="cyan",width=10)
        self.botaologin.place(x=170,y=80)
        self.botaocancelar = Button(master,text="Cancelar",bg="red",width=10)
        self.botaocancelar.place(x=255,y=80)
        self.botaologin.bind("<Button-1>",self.validar)
        self.botaocancelar.bind("<Button-1>",self.fechar)

    def validar(self,event):
        if self.val_usuario.get() == "user" and self.val_senha.get() == "123":
            showinfo("login","Bem vindo")
            self.fechar(event=None)
        else:
            if self.tentativas.get() == 2: 
                showinfo("login","Numero de tentativas excedeu o limite")
                self.fechar(event= None)
            else:
                root.setvar(name="tentativas",value=self.tentativas.get()+1)
    
    def fechar(self,event):
        root.destroy()


root = Tk()
root.geometry("400x150")
root.resizable(width=False, height=False)
window(root)

root.mainloop()