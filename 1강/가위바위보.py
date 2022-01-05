import random

def checkWin(user, com):
    if user == '가위':
            if com == '가위':
                print("비겼습니다!! ㄷㄷㄷ...")
            elif com == '바위':
                print("COM님이 승리하셨습니다...")
            else:
                print("User1님이 승리하셨습니다!!")
    elif user == "바위":
        if com == "가위":
            print("User1님이 승리하셨습니다!")
        elif com == '바위':
            print("비겼습니다!! ㄷㄷㄷ...")
        else:
            print("COM님이 승리하셨습니다...")
    else:
        if com == "가위":
            print("COM님이 승리하셨습니다...")
        elif com == "바위":
            print("User1님이 승리하셨습니다!!")
        else:
            print("비겼습니다!! ㄷㄷㄷ...")
