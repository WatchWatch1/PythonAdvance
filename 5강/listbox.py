from tkinter import *
win = Tk()
win.geometry("200x350")
win.title("내가 좋아하는 음식들의 리스트")

음식들 = ["피자", "자장면", "탕수육", "라면", "김치볶음밥", "참치마요 볶음밥"]

def 초기화():
    listb.delete(0,END)
    for 음식 in 음식들:
        listb.insert(END, 음식)
def 추가():
    listb.insert(END, entry.get())
def 삭제():
    listb.curselection()
    listb.delete(listb.curselection())
def 모두삭제():
    listb.delete(0, END)
def 출력():
    y = listb.get(0, END)
    print(y)

label = Label(win, text ="내가 좋아하는 음식 리스트")
label.pack()
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

listb = Listbox(win, selectmode="single")
listb.pack()

entry = Entry(win, bg="light blue")
entry.pack()

btn1 = Button(win, text="추 가", command = 추가)
btn1.pack()
btn2 = Button(win, text= "삭 제", command = 삭제)
btn2.pack()
btn3 = Button(win, text= "모두삭제", command = 모두삭제)
btn3.pack()
btn4 = Button(win, text = "초기화", command = 초기화)
btn4.pack()
btn5 = Button(win, text = "출 력", command = 출력)
btn5.pack()

sb.configure(command=listb.yview)
listb.configure(yscrollcommand=sb.set)

win.mainloop()
