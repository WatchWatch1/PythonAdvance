from tkinter import *
win = Tk()

win.geometry("500x500")
win.title("고래코딩임..")
win.option_add("*Font", "210세잎클로버 25")
win.configure(background="blue")

lbl = Label(win, text="이름을 입력하시오.")
lbl.pack()

txt = Entry(win)
txt.pack()

btn = Button(win, text="확인(OK)")
btn.pack()

win.mainloop()
