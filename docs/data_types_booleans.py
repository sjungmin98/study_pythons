bool_flag = True
type(bool)
# <class 'type'>
pass
bool_flag = False
type(bool_flag)
# <class 'bool'>

#문자 판단
#같음에 대한 기호 '=='
str_name = "Jungmin Seo"
str_name == "Jungmin Seo"
# True
str_name == "JungminSeo"
# False
#같지 않음에 대한 기호 '!='
str_name != "Jungmin Seo"
# False
str_name != "JungminSeo"
# True

#숫자에 대한 판단 (변수 + 부등호 + 기준값)
#컴퓨터 입장
#True = Yes = 1, False = No = 0
5 == 4
# False
5 != 4
# True
num_first = 5
num_first == 4
# False
num_first != 4
# True
num_first > 4   # 초과
# True
num_first >= 4  # 이상
# True

# if -elif - else
# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 90점 미만 : B, 나머지 : F
my_score = 90
my_score >= 90
# True
my_score = 89
my_score >= 90
# False
my_score > 80
# True
my_score = 80
my_score > 80
# False
pass