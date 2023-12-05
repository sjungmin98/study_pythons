height = int(input("키를 입력하세요. :"))/100
weight = int(input("몸무게를 입력하세요. :"))

BMI = weight / (height ** 2)

if BMI >= 25 :
    print("비만 입니다.")
elif BMI >= 23 :
    print("과체중 입니다.")
elif BMI >= 18 :
    print("정상체중 입니다.")   
else:
    print("저체중 입니다.")