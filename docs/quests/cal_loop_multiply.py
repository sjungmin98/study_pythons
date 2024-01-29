# 곱셈 계산기
def multiply(num_first, num_second): # 입력하는 값
    multiply_result=num_first*num_second
    return multiply_result # 나오는 값

# 곱셈 값 입력
cal_first=int(input("multiply first : "))
cal_second=int(input("multiply second : "))
 # 곱셈 값 출력
cal_multiply = multiply(cal_first, cal_second)
print_multiply_result=print("multiply result : {}".format(cal_multiply))
# 종료 사인 입력
q_sign_input=input("종료하려면 q를 입력하세요 : ")

# 종료될 때 까지 반복
while q_sign_input!='q' :
    # 곱셈 값 입력
    cal_first=int(input("multiply first : "))
    cal_second=int(input("multiply second : "))
    # 곱셈 값 출력1
    cal_multiply = multiply(cal_first, cal_second)
    print_multiply_result=print("multiply result : {}".format(cal_multiply))
    q_sign_input=input("종료하려면 q를 입력하세요 : ")
else:
    print("End Program!")



