# # input() 대한 기본 사용
# str_start = "start, Programming."
# print("{}"(str_start)) # 출력:
# str_input_desc = "영문 이름 입력 : "
# str_input = input("{}".format(str_input_desc)) # 입력
# pass # 종료

# input() 대한 숫자 받아 환산 하기
# 풀기 : 출생년도 입력 받아 나이 계산 
#예. 2023(올해) - 2000(출생년도) = 23(올해 나이)
str_start = "start, Programming."
print("{}".format(str_start)) # 출력:
str_input_desc = "출생년도 입력 : "
num_input_birthyear = input("{}".format(str_input_desc)) # 입력
num_age = 2023 - int(num_input_birthyear)
# num_age = print("출생년도 기준 내 나이 계산 : {}살".format(num_age))
print("출생년도 기준 내 나이 계산 : {}살".format(num_age))
pass # 종료  