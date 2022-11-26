#Aluno: Tulio Castro Silva

from tkinter import * 

class window:
    def __init__(self,master=None):
        #Variaveis
        self.val = DoubleVar(master,name="val")
        self.hist_sup = DoubleVar(master,name="hist_sup")
        self.hist_sub = DoubleVar(master,name="hist_sub")
        self.result = DoubleVar(master,name="result")
        self.operator = StringVar(master,name="operator")
        master.setvar(name="val",value=0.0)
        master.setvar(name="hist_sup",value=0.0)
        master.setvar(name="hist_sub",value=0.0)
        master.setvar(name="result",value="ans")
        master.setvar(name="operator",value="")
        #Visor
        self.visor = Frame(master,bg="#292929",width=300,height=200)
        self.visorsuperior = Frame(master,bg="#292929")
        self.sup_val = Label(self.visorsuperior,text="",font=("Arial",15),bg="#292929",fg="white",wraplength=290)
        self.sup_val.pack(side=LEFT)
        self.visorinferior = Frame(master,bg="#292929",width=150)
        self.sub_val= Label(self.visorinferior,text="",font=("Arial",20),bg="#292929",fg="white",wraplength=240)
        self.sub_val.pack(side=RIGHT)
        self.visorsuperior.place(x=0,y=0)
        self.visorinferior.place(x=0,y=80)
        self.visor.place(x=0,y=0)

        #Botoes

        #Linha 1
        self.botao_back = Button(master,text="←",font=("Arial",25),bg="#17CEE7",fg ="white",height=1,width=3)
        self.botao_back["border"] = "0"
        self.botao_back.place(x=0,y=150)
        self.botao_back.bind("<Button-1>",self.backspace)

        self.botao_CE = Button(master,text="CE",font=("Arial",25),bg="#17CEE7",fg ="white",height=1,width=3)
        self.botao_CE["border"] = "0"
        self.botao_CE.place(x=60,y=150)
        self.botao_CE.bind("<Button-1>",self.ce)

        self.botao_C = Button(master,text="C",font=("Arial",25),bg="#17CEE7",fg ="white",height=1,width=3)
        self.botao_C["border"] = "0"
        self.botao_C.place(x=120,y=150)
        self.botao_C.bind("<Button-1>",self.c)

        self.botao_div = Button(master,text="÷",font=("Arial",25),bg="#FB9AAB",fg ="white",height=1,width=3)
        self.botao_div["border"] = "0"
        self.botao_div.place(x=183,y=150)
        self.botao_div.bind("<Button-1>",self.div)

        #Linha 2
        self.botao7 = Button(master,text="7",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(7))
        self.botao7["border"] = "0"
        self.botao7.place(x=0,y=213)

        self.botao8 = Button(master,text="8",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(8))
        self.botao8["border"] = "0"
        self.botao8.place(x=60,y=213)

        self.botao9 = Button(master,text="9",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(9))
        self.botao9["border"] = "0"
        self.botao9.place(x=120,y=213)

        self.botao_mul = Button(master,text="x",font=("Arial",25),bg="#FB9AAB",fg ="white",height=1,width=3)
        self.botao_mul.place(x=183,y=213)
        self.botao_mul["border"] = "0"
        self.botao_mul.bind("<Button-1>",self.mul)

        #Linha 3
        self.botao4 = Button(master,text="4",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(4))
        self.botao4["border"] = "0"
        self.botao4.place(x=0,y=276)

        self.botao5 = Button(master,text="5",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(5))
        self.botao5["border"] = "0"
        self.botao5.place(x=60,y=276)

        self.botao6 = Button(master,text="6",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(6))
        self.botao6["border"] = "0"
        self.botao6.place(x=120,y=276)

        self.botao_neg = Button(master,text="-",font=("Arial",25),bg="#FB9AAB",fg ="white",height=1,width=3)
        self.botao_neg["border"] = "0"
        self.botao_neg.place(x=183,y=276)
        self.botao_neg.bind("<Button-1>",self.neg)

        #Linha 4
        self.botao1 = Button(master,text="1",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(1))
        self.botao1["border"] = "0"
        self.botao1.place(x=0,y=339)

        self.botao2 = Button(master,text="2",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(2))       
        self.botao2["border"] = "0"
        self.botao2.place(x=60,y=339)

        self.botao3 = Button(master,text="3",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero(3))
        self.botao3["border"] = "0"
        self.botao3.place(x=120,y=339)

        self.botao_pos = Button(master,text="+",font=("Arial",25),bg="#FB9AAB",fg ="white",height=1,width=3)
        self.botao_pos["border"] = "0"
        self.botao_pos.place(x=183,y=339)
        self.botao_pos.bind("<Button-1>",self.pos)

        #Linha 5
        self.botao0 = Button(master,text="0",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command= lambda: self.numero(0))
        self.botao0["border"] = "0"
        self.botao0.place(x=60,y=402)

        self.botao_dot = Button(master,text=".",font=("Arial",25),bg="#3F3F3F",fg ="white",height=1,width=3,command=lambda: self.numero("."))
        self.botao_dot["border"] = "0"
        self.botao_dot.place(x=120,y=402)

        self.botao_eq = Button(master,text="=",font=("Arial",25),bg="#FB9AAB",fg ="white",height=1,width=3)
        self.botao_eq["border"] = "0"
        self.botao_eq.place(x=183,y=402)
        self.botao_eq.bind("<Button-1>",self.eq)

    def backspace(self,event):
        palavra = self.sub_val["text"]
        self.sub_val["text"] = palavra[:-1]
    
    def ce(self,event):
        self.sub_val["text"] = ""
    
    def c(self,event):
        self.sub_val["text"] = ""
        self.sup_val["text"] = ""    
        root.setvar("operator",value="")   
        root.setvar("result","ans")
        root.setvar("val",0.0)

    def div(self,event):
        if root.getvar("operator") == "":
            self.sup_val["text"] = "{} -".format(self.sub_val["text"])
            root.setvar("val",value=float(self.sub_val["text"]))
            self.sub_val["text"] = ""
            root.setvar("operator",value="/")
        elif root.getvar("operator") != "/" and root.getvar("result") == "ans": 
            self.sup_val["text"] = self.sup_val["text"].replace((self.sup_val["text"][len(self.sup_val["text"])-1]),"/")
            root.setvar("operator","/")
        else:
             self.sup_val["text"] = "{} ÷".format(root.getvar("result"))
             root.setvar("operator","/")
             root.setvar("result","ans")
             self.sub_val["text"] = ""

    def mul(self,event):
        if root.getvar("operator") == "":
            self.sup_val["text"] = "{} x".format(self.sub_val["text"])
            root.setvar("val",value=float(self.sub_val["text"]))
            self.sub_val["text"] = ""
            root.setvar("operator",value="x")
        elif root.getvar("operator") != "x" and root.getvar("result") == "ans": 
            self.sup_val["text"] = self.sup_val["text"].replace((self.sup_val["text"][len(self.sup_val["text"])-1]),"x")
            root.setvar("operator","x")
        else:
             self.sup_val["text"] = "{} x".format(root.getvar("result"))
             root.setvar("operator","x")
             root.setvar("result","ans")
             self.sub_val["text"] = ""

    def pos(self,event):
        if root.getvar("operator") == "":
            self.sup_val["text"] = "{} +".format(self.sub_val["text"])
            root.setvar("val",value=float(self.sub_val["text"]))
            self.sub_val["text"] = ""
            root.setvar("operator",value="+")
        elif root.getvar("operator") != "+" and root.getvar("result") == "ans": 
            self.sup_val["text"] = self.sup_val["text"].replace((self.sup_val["text"][len(self.sup_val["text"])-1]),"+")
            root.setvar("operator","+")
        else:
             self.sup_val["text"] = "{} +".format(root.getvar("result"))
             root.setvar("operator","+")
             root.setvar("result","ans")
             self.sub_val["text"] = ""
    

    def neg(self,event):
        if root.getvar("operator") == "":
            self.sup_val["text"] = "{} -".format(self.sub_val["text"])
            root.setvar("val",value=float(self.sub_val["text"]))
            self.sub_val["text"] = ""
            root.setvar("operator",value="-")
        elif root.getvar("operator") != "-" and root.getvar("result") == "ans": 
            self.sup_val["text"] = self.sup_val["text"].replace((self.sup_val["text"][len(self.sup_val["text"])-1]),"-")
            root.setvar("operator","-")
        else:
             self.sup_val["text"] = "{} -".format(root.getvar("result"))
             root.setvar("operator","-")
             root.setvar("result","ans")
             self.sub_val["text"] = ""
    
    def numero(self,val):
        if len(self.sub_val["text"]) < 18:
            self.sub_val["text"] += str(val)

    def eq(self,event):

        if root.getvar("result") == "ans":
            val_sup = root.getvar("val")
            val_sub = float(self.sub_val["text"])
            root.setvar("hist_sub",val_sub)
        else:
            val_sup = root.getvar("hist_sup")
            val_sub = root.getvar("hist_sub")
            self.sup_val["text"] = "{} {}".format(root.getvar("val"),root.getvar("operator"))

        if root.getvar("operator") == "/":
            result = val_sup / val_sub
            self.sup_val["text"] += " {} = ".format(val_sub)
            root.setvar("hist_sup",result)
            root.setvar("val",result)
            self.sub_val["text"] = str(result)
            

        if root.getvar("operator") == "x":
            result = val_sup * val_sub
            self.sup_val["text"] += " {} = ".format(val_sub)
            root.setvar("hist_sup",result)
            root.setvar("val",result)
            self.sub_val["text"] = str(result)

        if root.getvar("operator") == "-":
            result = val_sup - val_sub
            self.sup_val["text"] += " {} = ".format(val_sub)
            root.setvar("hist_sup",result)
            root.setvar("val",result)
            self.sub_val["text"] = str(result)

        if root.getvar("operator") == "+":
            result = val_sup + val_sub
            self.sup_val["text"] += " {} = ".format(val_sub)
            root.setvar("hist_sup",result)
            root.setvar("val",result)
            self.sub_val["text"] = str(result)
        root.setvar("result",result)

        
root = Tk()
root.geometry("246x465")
root.title("CALCULATOR")
root.configure(bg="#3F3F3F")
root.resizable(width=False, height=False)
window(root)

root.mainloop()