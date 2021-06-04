from tkinter import * #python3

def setLabText():
    lab1.config(text="Hello world!!")

win = Tk()
win.title("First Python window")
win.geometry("600x400+200+100") #乘不是*
win.config(bg="#112233")

lab1 = Label(win, text="*v*", width=12, height=3, bg="#445566")
lab1.pack()

btn1 = Button(win, text="test", command=setLabText)
btn1.pack()

btnExit = Button(win, text="Exit", command=win.destroy)
btnExit.pack()


win.mainloop() 