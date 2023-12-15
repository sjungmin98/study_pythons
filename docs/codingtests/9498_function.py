# https://www.acmicpc.net/problem/9498
# 문제
## 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력
## 시험 성적을 출력한다.

# test_score = int(input())

# if test_score >= 90:
#     print("A")
# elif test_score >= 80:
#     print("B")
# elif test_score >= 70:
#     print("C")
# elif test_score >= 60:
#     print("D")
# else:
#     print("F")

def return_grade(test_score):  # 자신을 불렀을 때 값들 들어감.(순서 매칭)
    test_grade = ''
    if test_score >= 90:
        test_grade = 'A'
    elif test_score >= 80:
        test_grade = 'B'
    elif test_score >= 70:
        test_grade = 'C'
    elif test_score >= 60:
        test_grade = 'D'
    else:
        test_grade = 'F'
    return test_grade

test_score = int(input())
str_grade = return_grade(test_score)    # 호출 시 값들이 넘어감
print("{}".format(str_grade))
