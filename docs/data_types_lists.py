# 사용 이유 : 값들의 모임을 쉽게 전달
# 숫자 5개 값들로 이루어진 리스트
list_numerics = [0, 1, 2, 3, 4]      #5개수 값으로 이루어진 리스트
# 문자 3개 값들로 이루어진 리스트
list_fruits = ["apple", "banana", "cherry"]
#숫자와 문자 섞은 리스트 -> 우린 쓰지 않는다
list_mixs = [0, 1, 2, 3, "apple", "banana",]

len(list_numerics)
# 5
len(list_mixs)
# 6

## for문 활용 후 다시 오기

#  index(색인 위치값)
list_fruits = ["melon", "apple", "banana", "cherry"]
## index로 값 가져오기
list_fruits[0]  # 단일 변수로 여김 1차원(행)
# 'melon'
list_fruits[3]  # list_fruits_3
# 'cherry'

## error 발생
# list_fruits[4]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range

##설문 답변 받기
# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?            index 0
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타     index 1
# 당신의 답변 : A
# # 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?            index 2
# # A. Python B. Java C. JavaScript D. C++ E. 기타        index 3
# 당신의 답변 : B
# # 3.개발자에게 인기 있는 프로그래밍 언어는 무엇입니까?      index 4
# # A. Python B. Java C. JavaScript D. C++ E. 기타        index 5
# 당신의 답변 : E

list_polls = ["1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
    ,"A. Windows B. macOS C. Linux D. Chrome OS E. 기타" #답항에 내용 5개
    ,"2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
    ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
    ,"3.개발자에게 인기 있는 프로그래밍 언어는 무엇입니까?"
    ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
    ]

list_statistics = [0, 0, 0, 0, 0]   # 답항 내용 갯수만큼 0을 넣어줌
for num_count in [0,2,4]:
    str_question = list_polls[num_count]
    print ("{}".format(str_question))
    str_answer = list_polls[num_count+1]
    print ("{}".format(str_answer))

    str_question_result = input("당신의 답변(A~E를 순서 맞게 번호로 입력) : ")
    num_question_result = int(str_question_result) # 문자를 숫자로 변환
    index = num_question_result - 1 # index 위치 값 적용
    list_statistics[index] = list_statistics[index] + 1 # index 위치를 몇번 선택했는지 확인 할 수 있음

    print("-----------------")
    pass
