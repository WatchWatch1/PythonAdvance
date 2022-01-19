from tkinter import *

win = Tk()
win.geometry("1000x600")
win.title("라벨 사용해보기")

label1 = Label(win, text= "귀여운 강아지 사진", font=("굴림체", "20"), background=("purple"), foreground=("yellow"))
label1.pack()

img = PhotoImage(file = "dog.png")
label2 = Label(win, image = img)
label2.pack()

win.mainloop()
