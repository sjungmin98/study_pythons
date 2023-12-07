## 나오는 값 처리    
# first = 5
# second = 4
# sum = first + second
# return 0
def add() :
    first = 5
    second = 4
    sum = first + second
    # return 0
    return sum  # 상수 대신 변수 사용

# num_sum = 0
num_sum = add()
print("add return 결과 : {}".format(num_sum))

# num_first = 4
# num_second = 5
# # 곱셈 연산
# num_first * num_second

#두 수를 곱해서 결과 return
def multiply() :
    num_first = 4
    num_second = 5
    ## 곱셈 연산
    result = num_first * num_second   
    return result

num_multiply = multiply()
print("multiply 결과 : {}".format(num_multiply))

list_fruits = ["melon", "apple", "banana", "cherry"]
## index로 값 가져오기
list_fruits[0]  # 단일 변수로 여김 1차원(행)
def return_list() : 
    list_fruits  = ["melon", "apple", "banana", "cherry"]
    return list_fruits
print("return_list() return result : {}".format(return_list()))

# list 중에 index로 값 return
def return_listbyindex() :
    list_fruits  = ["melon", "apple", "banana", "cherry"]
    list_fruits[0]  
    return list_fruits[0]

print("return_listbyindex() return result : {}".format(list_fruits[0]))

# my_score = 79
# if my_score >= 90 : # 90점 이상 : A
#     print("{}은 90점 이상으로 A 학점.".format(my_score))
# elif my_score > 80 :    # 80점 초과 : B
#     print("{}은 80점 초과로 B 학점.".format(my_score))
# else :  # 나머지 : F
#     print("{}은 80점 이하이므로 F 학점.".format(my_score))
# 반복 print 작업을 줄이기
def return_grade(my_score):
    my_grade = ''
    if my_score >= 90:  # 90점 이상 : A
        my_grade = 'A'
    elif my_score > 80:  # 80점 초과 : B
        my_grade = 'B'
    else:  # 나머지 : C
        my_grade = 'C'
    return my_grade

str_grade = return_grade(99)
print("당신의 학점 : {}".format(str_grade))































































