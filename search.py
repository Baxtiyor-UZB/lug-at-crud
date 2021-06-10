from tkinter import *

root=Tk()
root.title('UZ<==>Eng')
root.geometry('700x600')
root.config(bg='pink')
root.resizable(0,0)

def home():
    root.destroy()
    import lugat
e1=Entry(root,font=("italic 40 bold"),fg='#000000' ,border=10,background='lightblue')
e1.place(x=60,y=0)
def searching():
    import sqlite3
    conn = sqlite3.connect('soz.db')
    conn.commit()
    cursor = conn.execute("SELECT eng from uzen where uz =='{}'".format(e1.get()) )
    s=cursor.fetchall()
    text.insert(END, s)
    conn.close()
    


Button(root,text='               SEARCHING             ',border=10,font=("italic 30 bold"),fg='green' ,background='#ffffff',command=searching).place(x=60,y=85)
Button(root,text='                HOME                      ',border=10,font=("italic 30 bold"),fg='green' ,background='#ffffff',command=home).place(x=60,y=455)
text=Text(root,width=25,border=10, height=5,font=("italic 31 bold"),fg='red' ,background='green')

text.place(x=60,y=180)
root.mainloop()