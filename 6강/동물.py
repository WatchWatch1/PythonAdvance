from tkinter import * 
from tkinter import messagebox 

def check1():  # 선택하면 1, 비선택이면 0입니다 
    str = "" 
    if checkVar1.get() == 1: 
        str = str + "고양이" 
    if checkVar2.get() == 1: 
        str = str + " 강아지" 
    if checkVar3.get() == 1: 
        str = str + " 토끼" 
    if checkVar4.get() == 1: 
        str = str + " 햄스터" 
    if checkVar5.get() == 1:
        str = str + " 앵무새"
    if str=='': 
        show1.config(text = "다 싫어요") 
    else: 
        messagebox.showinfo("메시지", str + "를 좋아합니다") 
def end1(): 
    win.destroy() 

win = Tk() 
win.title("좋아하는 동물 선택") 
win.geometry("500x300") 

# 체크 버튼 데이터가 저장될 변수 생성
checkVar1 = IntVar() 
checkVar2 = IntVar() 
checkVar3 = IntVar() 
checkVar4 = IntVar() 
checkVar5 = IntVar()

label1 = Label(win, text = "[1번 문제] 당신이 가장 좋아하는 동물을 모두 선택하세요 ") 
label1.pack() 

cb1 = Checkbutton(win, text = "1. 고양이", variable=checkVar1) 
cb1.pack() 
cb2 = Checkbutton(win, text = "2. 강아지", variable=checkVar2) 
cb2.pack() 
cb3 = Checkbutton(win, text = "3. 토끼", variable=checkVar3) 
cb3.pack() 
cb4 = Checkbutton(win, text = "4. 햄스터", variable=checkVar4) 
cb4.pack()
cb5 = Checkbutton(win, text = "5. 앵무새", variable=checkVar5) 
cb5.pack()

show1=Label(win, text = "여기에 출력됩니다") 
show1.pack() 

확인버튼 = Button(win, text ="확 인", width=10, command=check1) 
확인버튼.pack() 
종료버튼 = Button(win, text ="종 료", width=10, command=end1) 
종료버튼.pack() 

win.mainloop()
