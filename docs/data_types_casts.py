# pass
type("Jungmin") #문자 type
# <class 'str'>
type(1998) #숫자 type
# <class 'int'>

name = "Jungmin" #문자 type
type(name)
# <class 'str'>

age = 26 #숫자 type
type(age)
# <class 'int'>

# 터미널 입력 값에 대한 확인
str_input = input("문자 입력 : ")
print("입력({}) type 표시 : {}".format(str_input, type(str_input)))
num_input = input("숫자 입력 : ")
print("입력({}) type 표시 : {}".format(num_input, type(num_input)))
# cast : changing data type
int(num_input)
1998
type(int(num_input))
# <class 'int'>

# cast 불가한 경우
mix_val = "23k"
int(mix_val)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '23k'
pass