from tkinter import *

def play():
    global time

    시작버튼.place(x=1000099999900, y=999999999999999999)
    누르기버튼.place(x=60, y=80)

    time = time - 1
    시간.config(text="남은 시간 {}초".format(time))
    win.after(1000, play)

win = Tk()
win.title("버튼누르기")
win.geometry("200x200+500+100")

time = 10
count = 0


타이틀 = Label(win, text = "버튼 빨리 누르기")
타이틀.pack()
시간 = Label(win, text="남은 시간 {}초".format(time))
시간.pack()
점수 = Label(win, text=count)
점수.pack()

누르기버튼 = Button(win, text="누르세요" , width=10, height=2, command=play)
시작버튼 = Button(win, text="시작", width=10, height=2, command=play)
시작버튼.place(x=60, y=80)

win.mainloop()
