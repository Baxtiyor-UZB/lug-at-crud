from tkinter import *
from tkinter import messagebox
import time
t=list(time.localtime())

while (t[0]==2021 and t[1]==4 and t[2]>=19):
    
    root=Tk()
    root.title('UZ<==>Eng')
    root.geometry('700x500')
    root.config(bg='orange')
    root.resizable(0,0)
    #funksiyalar
    def search():
        root.destroy()
        import search
    def yarat():
        root.destroy()
        import create

    #Tugmalar
    Button(root,text=' You can use dictionary ',font=("italic 40 bold"),fg='green' ,background='orange',command=search).place(x=20,y=100)
    Button(root,text='    Create    ',font=("italic 20 bold"),fg='green' ,background='orange',command=yarat).place(x=35,y=350)
    Button(root,text='    Base      ',font=("italic 20 bold"),fg='green' ,background='orange').place(x=200,y=350)
    Button(root,text='   Update  ',font=("italic 20 bold"),fg='green' ,background='orange').place(x=365,y=350)
    Button(root,text='   Delete  ',font=("italic 20 bold"),fg='green' ,background='orange').place(x=520,y=350)





    root.mainloop()
messagebox.showinfo("dasturdan foydalanish vaqti tugagan!")