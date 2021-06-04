from tkinter import * #python3
from random import randint

def set_lab():
    
    x = randint(1,1000)
    lab.config(text=x)

win = Tk()
win.title("Python window")
win.geometry("600x400+200+100") #乘不是*
win.config(bg="#112233")

lab = Label(win, text="0", width=12, height=3, bg="yellow")
lab.pack()

btn_G = Button(win, text="Generate", command=set_lab)
btn_G.pack()

btnExit = Button(win, text="Exit", command=win.destroy)
btnExit.pack()










win.mainloop() 