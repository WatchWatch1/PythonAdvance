from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("사칙 연산 프로그램")

def click1(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) + int(txt2) 
    label3.config(text = (txt1) + " + " + (txt2) + " = " + str(answer)) 
def click2(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) - int(txt2) 
    label3.config(text = (txt1) + " - " + (txt2) + " = " + str(answer)) 
def click3(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) * int(txt2) 
    label3.config(text = (txt1) + " x " + (txt2) + " = " + str(answer)) 
def click4(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) / int(txt2) 
    label3.config(text = (txt1) + " / " + (txt2) + " = " + str(answer)) 
def click5(): 
    label3.config(text = "두 수의 계산 결과는?") 
    entry1.delete(0, END) 
    entry2.delete(0, END) 
def click6(): 
    win.destroy() 

label1 = Label(win, text = "수 입력 1 ") 
label1.grid(row=0, column=0) 
entry1 = Entry(win, width = 10, bg = "light green") 
entry1.grid(row=0, column = 1) 
label2 = Label(win, text = "수 입력 2 ") 
label2.grid(row=1, column=0) 
entry2 = Entry(win, width = 10, bg = "light blue") 
entry2.grid(row=1, column = 1) 
button1 = Button(win, text = " + ",width = 8, command = click1) 
button1.grid(row=2, column=0) 
button2 = Button(win, text = " - ",width = 8, command = click2) 
button2.grid(row=2, column=1) 
button3 = Button(win, text = " X ", width = 8, command = click3) 
button3.grid(row=2, column=2) 
button4 = Button(win, text = " / ",width = 8, command = click4) 
button4.grid(row=2, column=3) 
label3 = Label(win, text = "두 수의 계산 결과는?") 
label3.grid(row=3, column=1, columnspan=3) 
button5 = Button(win, text = " 지우기 ",width = 8, command = click5) 
button5.grid(row=4, column=2) 
button5 = Button(win, text = " 종 료 ",width = 8, command = click6) 
button5.grid(row=5, column=2)

win.mainloop()
