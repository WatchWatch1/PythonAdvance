from socket import MsgFlag
from tkinter import *
from tkinter import messagebox as msg

window = Tk()
window.geometry('300x500')
window.title("메시지박스")

def msg1():
    str = msg.askquestion("메시지상자", "프로그램을 종료할까요?")
    if str == "yes":
        window.destroy()
    else:
        msg.showinfo("메시지상자", "취소버튼을 \n누르셨습니다.")

def msg2():
    window.destroy()
    window.quit()

def msg3():
    msg.showerror("메시지상자", "버튼 로딩에 실패하였습니다.")

def msg4():
    msg.showwarning("메시지상자", "                 (경고!) \n\n\n컴퓨터에 바이러스가 확인되었습니다.")

def msg5():
    msg.askyesno("메시지상자", "메시지가 종료됩니다.")

Bu1=Button(window, text="물음", width = 10, command=msg1)
Bu1.pack(pady=5)
Bu2=Button(window, text="리로딩 실패", width = 10, command=msg3)
Bu2.pack(pady=5)
Bu3=Button(window, text="경고문자", width = 10, command=msg4)
Bu3.pack(pady=5)
Bu4=Button(window, text="확인취소", width = 10, command=msg5)
Bu4.pack(pady=5)
Bu7=Button(window, text="종료", width = 10, command=msg2)
Bu7.pack(pady=5)

window.mainloop()
