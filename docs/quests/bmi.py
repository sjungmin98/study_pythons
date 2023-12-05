height = int(input("키를 입력하세요. :")) / 100
weight = int(input("몸무게를 입력하세요. :"))

BMI = weight / (height ** 2)

if BMI >= 25 :
    print("당신의 BMI 수치는{}, 비만 입니다.".format(BMI))
elif BMI >= 23 :
    print("당신의 BMI 수치는{}, 과체중 입니다.".format(BMI))
elif BMI >= 18 :
    print("당신의 BMI 수치는{}, 정상체중 입니다.".format(BMI))   
else :
    print("당신의 BMI 수치는{}, 저체중 입니다.".format(BMI))