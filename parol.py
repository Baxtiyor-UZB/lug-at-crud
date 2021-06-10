from tkinter import *
import uuid
root=Tk()
root.geometry('600x600')
e=Entry(root)
e.place(x=100,y=100)
a=hex(uuid.getnode())
Label(root,text=str(a),font=("arial 40 bold")).pack()
def parol():
    a=uuid.getnode()
    print(a)
    x=a//385
    y=a%385
    a=x+y
    if str(e.get())==str(a):
        root.destroy()
        import lugat
        
        
Button(root,text='kirish',command=parol).place(x=100,y=200)
root.mainloop()
