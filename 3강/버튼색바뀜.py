from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("배경색 바꾸기")


def click1(): 
    win.configure(background='red') 
 
def click2():
    win.configure(background="blue")

def click3():
    win.configure(background="yellow")

def click4():
    win.configure(background="purple") 
 
Label1 = Label(win, text = "버튼을 클릭해서 바탕화면의 색을 바꿔보세요!") 
Label1.pack() 


Button1 = Button(win, text="빨간색", width=7, command=click1) 
Button1.pack() 
Button2 = Button(win, text="파란색", width=7, command=click2)
Button2.pack() 
Button3 = Button(win, text="노란색", width=7, command=click3)
Button3.pack() 
Button4 = Button(win, text="보라색", width=7, command=click4)
Button4.pack() 
win.mainloop()
