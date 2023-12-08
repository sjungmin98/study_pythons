def multiplication(number):
    for number_first in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        result = number * number_first
        print("{} x {} = {}".format(number, number_first, result))

def multiply_result(number, user_input):
    result = number * int(user_input)
    print("result for {}dan: {}".format(number, result))

def cal_multi():
    numbers = [20, 30, 35]

    for number in numbers:
        multiplication(number)

    print("-----------------------------")

    while True:
        for number in [20, 30, 35]:
            user_input = input("{} * ".format(number))

            if user_input == 'q':
                print("Quit the calculator")
                return

            multiply_result(number, user_input)

cal_multi()