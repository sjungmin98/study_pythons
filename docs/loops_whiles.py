# condition이 True 동안 동작
# while True :
#     pass

#while 정지 1 case with break문 사용
num_virtual = 0
while True :
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    if num_virtual >= 5 :
        pass
        break
    pass


# while 정지 2 case without break문 사용
num_virtual = 0
while 5 > num_virtual :
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    pass
print("End Program!")

# 풀기 : 5 구구단 결과 매번 출력