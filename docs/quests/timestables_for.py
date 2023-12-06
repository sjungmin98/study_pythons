num = 5
num_vir = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in num_vir:
    result = num * number
    pass
    print("{} x {} = {}".format(num, number, result))
pass    
gugudan = int(input("숫자를 입력하세요 "))
num = 1
for number in num_vir:
    result = gugudan * num
    pass
    print("{} x {} = {}".format(gugudan, num, result))
    num += 1
pass
print("End Program!")