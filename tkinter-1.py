from tkinter import * #python3

x = 0

def Add_lab():
    global x
    x+=1
    lab.config(text=x)

def Sub_lab():
    global x
    x-=1
    lab.config(text=x)

win = Tk()
win.title("Python window")
win.geometry("600x400+200+100") #乘不是*
win.config(bg="#112233")

lab = Label(win, text="0", width=12, height=3, bg="#ffffff")
lab.pack()

btn_add = Button(win, text="Add", command=Add_lab)
btn_add.pack()

btn_sub = Button(win, text="Sub", command=Sub_lab)
btn_sub.pack()


btnExit = Button(win, text="Exit", command=win.destroy)
btnExit.pack()










win.mainloop() 