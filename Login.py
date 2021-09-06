from tkinter import *
#Janela 
root = Tk()
root.geometry('350x350')

#Funções
def click():
    
    add = e.get()
    sen = e_2.get()
    if(add == "" or sen == ""):
        
        my_Label3 = Label(root,text = "Unfilled field").pack()
        
        
    else:
        my_Label3 = Label(root,text = "Login: " + str(add)).pack()
        my_Label3 = Label(root,text = "Senha: " + str(sen)).pack()
       
    
#Labels
my_Label = Label(root,text = "Login:", font="Arial" )
my_Label.pack()
#Entradas
e = Entry(root, width = 25)
e.pack()
my_Label2 = Label(root, text = "Senha:",font = "Arial")
my_Label2.pack()
e_2 = Entry(root, width = 25,)
e_2.pack()
#Botão
my_Button = Button(root, text = "Register",font="Arial", command=click)
my_Button.pack()



root.mainloop()