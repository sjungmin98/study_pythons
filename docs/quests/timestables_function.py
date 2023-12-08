def multiply(number, multiplier):
    return number * multiplier

def cal_multi():
    numbers = [20, 30, 35]

    for number in numbers:
        num = 1
        while num <= 9:
            result = multiply(number, num)
            print("{} x {} = {}".format(number, num, result))
            num += 1

cal_multi()

print("-----------------------------")

def multiply_and_print(number):
    multiplier = int(input("{} * ".format(number)))
    if multiplier == 'q':
        print("Quit the calculator")
        return None
    result = multiply(number, multiplier)
    print("Result for {}: {}".format(number, result))

def cal_multi_input():
    numbers = [20, 30, 35]

    for number in numbers:
        multiply_and_print(number)

cal_multi_input()