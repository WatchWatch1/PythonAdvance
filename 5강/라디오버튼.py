from tkinter import *

win = Tk()
win.geometry("350x400")
win.title("좋아하는 동물 선택")

라디오버튼그룹 = IntVar()
label1 = Label(win, text = "[1번문제] 당신이 좋아하는 동물은?")
label1.pack()
rb1 = Radiobutton(win, text= "1. 고양이", variable=라디오버튼그룹, value=1)
rb1.pack()

rb2 = Radiobutton(win, text= "2. 강아지", variable=라디오버튼그룹, value=2)
rb2.pack()

rb3 = Radiobutton(win, text= "2. 토끼", variable=라디오버튼그룹, value=3)
rb3.pack()
