def multiply(num_first, num_second):
    return num_first * num_second

def cal_multi():
    while True:
        num_first = input("first: ")
        num_second = input("second: ")

        if num_first == 'q' or num_second == 'q':
            print("Quit the calculator")
            break

        num_first = int(num_first)
        num_second = int(num_second)
        result = multiply(num_first, num_second)
        print("result: {}".format(result))

cal_multi()


