from tkinter import *
from datetime import datetime

win = Tk()
win.geometry("400x400")
win.title("현재 시각")

def time():
    print(datetime.now())


btn = Button(win)
btn.config(width = 20, height = 5)
btn.config(text = "현재 시각")
btn.config(command = time)
btn.pack()

win.mainloop()
