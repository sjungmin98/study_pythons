# 기본 if elif else 구문
# if True : 
#     pass
# elif True :
#     pass
# else :
#     pass

#문자 비교
str_name="oh jisu"
str_name=="oh jisu"

#문자에 대한 긍정으로 질문
if str_name=="oh jisu" : 
    pass
    print("name is {}.".format(str_name))
print("End Program!")

# if문의 질문 형식(condition=조건절): 변수+부등호+기준값
#문자에 대한 부정으로 질문
if str_name!="oh jisu" :  
    pass
    print("name is not {}.".format(str_name))
print("End Program!")

# if - else
# num_first >= 4 -> True : "큼", False : "작음"
num_first = 5
if num_first >= 4 : 
    pass    # condition이 True
    print("{}는 4보다 크다".format(num_first))
else :
    pass    # condition이 False
    print("{}는 4보다 작다".format(num_first))
print("End Program!")
pass

num_first = 5
if num_first >= 6 : 
    pass    # condition이 True
    print("{}는 6보다 크다".format(num_first))
else :
    pass    # condition이 False
    print("{}는 6보다 작다".format(num_first))
print("End Program!")
pass

# if - elif - else
# 점수에 따른 표시
# 90점 이상: A, 80점 초과: B, 나머지 F
pass
# my_score = 90


my_score = 79

if my_score >= 90 : # 90점 이상: A
    pass
    print("{}점은 90점 이상으로 A 학점.".format(my_score))
elif my_score > 80 : # 80점 초과: B
    pass
    print("{}점은 80점 초과이므로 B 학점.".format(my_score))
else :               # 나머지 F
    pass
    print("{}점은 80점 이하이므로 F 학점.".format(my_score))
    pass
print("End Program!")

# 부등호 사용 시 결과는 True or False (Boolean)


# if - elif - else
# 점수에 따른 표시
# 90점 이상: A, 80점 초과: B, 나머지 F

my_score=90
my_score>=90
#True
my_score=80
my_score>80
# False

# 컴퓨터는 condition을 판단할 때 논리 연산자(True or False)를 사용함.  
# 현재 값이 75점 이상부터 85점 이하는 C 학점이다.

# 논리(=True or False) 연산자(결과값)
# and : 1 and 1 --> 1, 나머지는 0
# or : 0 or 0 --> 0, 나머지는 1
# not : --> 반대로 변환 : False --> True / True --> False 

# 논리 연산자(True or False에 대한 결과값)
first = 200
second = 33
third = 500

# conditon 사용 전에는 각각 conditon의 결과값을 확인하기
first > second
# True
third > first
# True
(first > second) and (third > first)
# True

if (first > second) and (third > first) :
    print("Both conditions are True")
    pass

if not (first < second) :
    print("first > second")
    pass

print("End Program!")

