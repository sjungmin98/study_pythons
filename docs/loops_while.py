# condition이 True인 동안 동작
# 기본 while 구문 - if 문과 유사
# while True :
#     pass


# while 정지 1st case with break 문 사용
# 특정 시점을 정해놓지 않으면 while 문이 False가 될 때까지 반복
num_virtual=0
while True:
    pass
    num_virtual = num_virtual+1
    print("{} = num_virtual+1".format(num_virtual))
    if num_virtual>=5: # if - break: condition에 따라 정지
        pass
        break
    pass
print("End Program!")

# while 정지 2nd case without break문 사용
# 특정 시점을 정해놓지 않으면 while 문이 False가 될 때까지 반복
num_virtual=0
while num_virtual<5:
    pass
    num_virtual = num_virtual+1
    print("{} = num_virtual+1".format(num_virtual))
    pass
print("End Program!")

# 풀기: 구구단-5단 결과 매번 출력