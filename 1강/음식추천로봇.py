import random

벌칙 = ["노래 1곡 부르기", "엉덩이로 이름 쓰기", "뿅망치 맞기", "인디언 밥", "춤추기", "레고 맞추기", "안 쉬고 1km 뛰기", "30분 자전거 타기", "딱밤", "치킨빵", "피자빵", "햄버거빵", "김치싸대기", "싸대기 맞기"]


print("벌칙을 고르겠습니다! 마음의 준비를 하시길 바랍니다. (김치싸대기는 조심)")
print("벌칙 리스트")
print("="*50)
for 황금벌칙 in 벌칙:
    print(황금벌칙)
print("="*50)
pick = random.choice(벌칙)
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ {} 당첨!!!!".format(pick))

while True:
    user = input("다시 벌칙을 고를까요? (네/아니오) ")
    if user == "아니오":
        print("안녕히가세요!")
        break
    elif user == "네":
        print("벌칙을 다시 고르겠습니다! 마음의 준비 하세요!")
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요!") 
        continue

    pick = random.choice(벌칙)
    print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ {} 당첨!!!!".format(pick))
