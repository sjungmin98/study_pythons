#source from [study_pythons/docs/quests/timestables_fors.py]

def timestables(x) : # 'x'에 user의 input 받음
    numbering=[1, 2, 3, 5,  6, 7, 8, 9] # 9단까지만 실행
    if x=='20' :
        for loop in numbering: # 9단까지 반복 실행
            print("{}*{}={}".format(int(x), loop,(loop)*int(x))) # 구구단 포맷-출력/계산
    elif x=='30' :
        for loop in numbering: # 9단까지 반복 실행
            print("{}*{}={}".format(int(x), loop,(loop)*int(x))) # 구구단 포맷-출력/계산
    elif x=='35' :
         for loop in numbering: # 9단까지 반복 실행
            print("{}*{}={}".format(int(x), loop,(loop)*int(x))) # 구구단 포맷-출력/계산
    else :
        error_sign="잘못된 입력입니다."
        print("{}".format(error_sign))
    return stop() # 이후 무조건 stop() 실행시키기 위해 return stop()

def stop() : # 종료할지 말지 결정하는 function
    str_input=input("구구단 몇단(종료하려면 q 입력) : ") # 이전 input과 달리 종료 sign을 누를 수 있게 함
    if str_input !="q" : # user input이 q가 아닐 경우 timetables() 실행 - 안에 필요한 변수 입력함.
        timestables(str_input)
    else : # q가 나올 경우 종료
        print("End Program!")

# 초기 user input
stop()

