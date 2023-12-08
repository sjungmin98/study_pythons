def cal_multi():
    number_simple = 20
    num = 1

    while num <= 9 :
        result = number_simple * num
        print("{} x {} = {}".format(number_simple, num, result))
        num += 1
    
    number_simple = 30
    num = 1

    while num <= 9 :
        result = number_simple * num
        print("{} x {} = {}".format(number_simple, num, result))
        num += 1

    number_simple = 35
    num = 1
    
    while num <= 9 :
        result = number_simple * num
        print("{} x {} = {}".format(number_simple, num, result))
        num += 1
cal_multi()

print ("-----------------------------")

def multiply(num_first, num_second):
    return num_first * num_second

def multiply(num_third, num_fourth):
    return num_third * num_fourth

def multiply(num_fifth, num_sixth):
    return num_fifth * num_sixth

def cal_multi():
    while True:
        num_first = 20
        num_second = input("20 * ")
        num_third = 30
        num_fourth = input("30 * ")
        num_fifth = 35
        num_sixth = input("35 * ")

        if num_second == 'q' or num_fourth == 'q' or num_sixth == 'q':
            print("Quit the calculator")
            break
        
        num_second = int(num_second)
        num_fourth = int(num_fourth)
        num_sixth = int(num_sixth)

        result = multiply(num_first, num_second)
        result_30 = multiply(num_third, num_fourth)
        result_35 = multiply(num_fifth, num_sixth)

        print("result for 20dan: {}".format(result))
        print("result for 30dan: {}".format(result_30))
        print("result for 30dan: {}".format(result_35))

cal_multi()

