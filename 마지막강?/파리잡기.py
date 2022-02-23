from tkinter import *
from tkinter import messagebox
import random

id = None

def move():
    변경x = random.randint(100, 500)
    변경y = random.randint(100, 500)
    파리버튼.place(x=변경x, y=변경y)
    delay = random.randint(300, 1000)
    global id
    id = win.after(random.randint(250, 500), move)

def click():
    win.after_cancel(id)
    messagebox.showinfo("잡았당ㅇㅇ", "파리를 잡았네요. ㅊㅋㅊㅋ")
win = Tk()
win.title("파리잡기!ㅋ")
win.geometry("600x600")

img = PhotoImage(file="파리.png")
파리버튼 = Button(win, image=img, command = click)
파리버튼.place(x=300, y=300)

win.after(10, move)

btn = Button(win)
btn.config(width = 10, height = 3)
btn.config(text = "다시 시작")
btn.config(command = move)
btn.pack() 



win.mainloop()
