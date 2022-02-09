from tkinter import *
win = Tk()
win.geometry("200x350")
win.title("Todo List!!")

할일들 = ["아침밥 먹기", "학교 가기", "점심먹기", "학원 갈 준비 하기", "학원 가기", "학원 공부하기", "집 돌아가기", "숙제하기", "저녁먹기", "씻고 잘 준비하기", "꿈나라 가기"]

listb = Listbox(win, selectmode="single")
listb.pack()


def 할일삭제():
    listb.curselection()
    listb.delete(listb.curselection())

def 할일추가():
    listb.insert(END, entry.get())

def 모두삭제():
    listb.delete(0, END)

def 할일저장():
    y = listb.get(0, END)
    print(y)

entry = Entry(win, bg="light blue")
entry.pack()

sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

btn1 = Button(win, text="할일추가", command = 할일추가)
btn1.pack()
btn2 = Button(win, text= "할일삭제", command = 할일삭제)
btn2.pack()
btn4 = Button(win, text= "모두삭제", command = 모두삭제)
btn4.pack()
btn3 = Button(win, text= "할일저장", command = 할일저장)
btn3.pack()

sb.configure(command=listb.yview)
listb.configure(yscrollcommand=sb.set)

win.mainloop()
