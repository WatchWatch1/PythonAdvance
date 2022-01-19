from tkinter import *
win = Tk()

win.geometry("400x268")
win.title("라벨 사용해보기")

label1 = Label(win, text = "파이썬 공부하기", font=("궁서체", "24"), width=25, height=4, anchor=CENTER, foreground="Blue", background="yellow")

label1.pack()

label2 = Label(win, text = "고래코딩ㅇㅇ", font=("210세잎클로버", "24"), width=25,height=4, anchor=CENTER, foreground="Red", background="green")

label2.pack()

win.mainloop()
