from tkinter import *
from openpyxl import Workbook
#Janela 
root = Tk()
root.geometry('200x200')
#Workbook
wb = Workbook()
#Funções
def click():
    
    add = e.get()
    sen = e_2.get()
    if(add == "" or sen == ""):
        
        my_Label3 = Label(root,text = "Unfilled field").grid(row  = 7, column = 1)
    else:
        planilha = wb.worksheets[0]
        planilha['A1'] = "Nome"
        planilha ['A2'] = add
        planilha ['B1'] = "Senha"
        planilha ['B2'] = sen
        wb.save('.\ExcelSaves/File.xlsx')
        print("Save File.....")


        
       
    
#Labels
my_Label = Label(root,text = "Login:", font="Arial" )
my_Label.grid(row = 0, column = 1)
#Entradas
e = Entry(root, width = 25)
e.grid(row = 2,column = 1)
my_Label2 = Label(root, text = "Senha:",font = "Arial")
my_Label2.grid(row = 3, column = 1 )
e_2 = Entry(root, width = 25,)
e_2.grid(row = 4, column = 1 )
#Botão
my_Button = Button(root, text = "Register",font="Arial", command=click)
my_Button.grid(row = 5, column = 1)



root.mainloop()