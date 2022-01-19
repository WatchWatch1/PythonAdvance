from tkinter import *
win = Tk()

win.geometry("400x400")
win.title("버튼 사용해보기")

def alert():
    print("Python 알림: 버튼이 눌렸습니다.")

btn = Button(win)
btn.config(width = 20, height = 5)
btn.config(text = "버튼")
btn.config(command = alert)
btn.pack()


win.mainloop()
