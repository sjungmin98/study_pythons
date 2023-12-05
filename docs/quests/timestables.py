# - 구구단 5단 단계별 표시(while 문 사용)
# 예. 5 * 1= 5  5 * 2 = 10 ... 5 * 9 = 45
# # - option) 단수 입력 받아 연산

num_vir = 5
num = 1

while num <= 9 :
    result = num_vir * num
    print("{} x {} = {}".format(num_vir, num, result))
    num += 1
pass
gugudan = int(input("숫자를 입력하세요"))
num = 1

while num <= 9:
    result = gugudan * num
    print("{} x {} = {}".format(gugudan, num, result))
    num += 14