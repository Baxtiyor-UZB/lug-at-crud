from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import glob
a=glob.glob('*.db')
root=Tk()
root.title('UZ<==>Eng')
root.geometry('700x500')
root.config(bg='pink')
root.resizable(0,0)

Label(root,text='UZ',font=("italic 40 bold"),fg='#000000' ,border=10,background='pink').place(x=0,y=0)
Label(root,text='EN',font=("italic 40 bold"),fg='#000000' ,border=10,background='pink').place(x=0,y=100)
e1=Entry(root,font=("italic 40 bold"),fg='#000000' ,border=10,background='lightblue')
e1.place(x=100,y=0)
e2=Entry(root,font=("italic 40 bold"),fg='#000000' ,border=10,background='lightblue')
e2.place(x=100,y=100)
tarjima=e1.get()
def create():
    x=0
    if 'soz.db' not in a:

        conn = sqlite3.connect('soz.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS uzen")

        query = "CREATE TABLE uzen(uz CHAR(30) NOT NULL,eng CHAR(30) NOT NULL )"
        cursor.execute(query)

        conn.commit()
        conn.close()
    
    else:
        x=1
    
    
    conn = sqlite3.connect('soz.db')
    conn.execute("INSERT INTO uzen(uz, eng) "
                "VALUES ('{}', '{}')".format(e1.get(),e2.get()))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("so'z bazaga muvaffaqiyatli qo'shildi!")
    root.destroy()
    import lugat
    


Button(root,text='                    creating                 ',border=10,font=("italic 30 bold"),fg='green' ,background='#ffffff',command=create).place(x=60,y=385)

root.mainloop()