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

#기본 구문
# for x in [] :
#     print()

# 문자 3개 값들로 이루어진 리스트 
for x in ["apple", "banana", "cherry"]: #반복 대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(x))

list_fruits = ["apple", "banana", "cherry"]
for str_fruit in list_fruits: #반복 대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(str_fruit))

numerics = [0, 1, 2, 3, 4]      #5개수 값으로 이루어진 리스트
for number in numerics :
    pass
    print("Number : {}".format(number+2))
print("End Program!")

