from tkinter import * #python3
from random import randint

def set_lab():
    x = randint(1,43)
    data = [0]*6
    i=0
    while i<6:
        x = randint(1,43)
        flag = True
        j  = 0
        while j<i and flag:
            if data[j]==x:
                flag = False
            j+=1
        if flag:
            data[i]=x
            i+=1
    lab1.config(text=data[0])
    lab2.config(text=data[1])
    lab3.config(text=data[2])
    lab4.config(text=data[3])
    lab5.config(text=data[4])
    lab6.config(text=data[5])

win = Tk()
win.title("Python window")
win.geometry("600x400+200+100") #乘不是*
win.config(bg="#112233")

lab1 = Label(win, text="0", width=12, height=3, bg="#445566")
lab1.pack()
lab2 = Label(win, text="0", width=12, height=3, bg="#445566")
lab2.pack()
lab3 = Label(win, text="0", width=12, height=3, bg="#445566")
lab3.pack()
lab4 = Label(win, text="0", width=12, height=3, bg="#445566")
lab4.pack()
lab5 = Label(win, text="0", width=12, height=3, bg="#445566")
lab5.pack()
lab6 = Label(win, text="0", width=12, height=3, bg="#445566")
lab6.pack()

btn_G = Button(win, text="Generate", command=set_lab)
btn_G.pack()

btnExit = Button(win, text="Exit", command=win.destroy)
btnExit.pack()










win.mainloop() 