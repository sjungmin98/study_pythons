def calculator(operation, num1, num2):
    return operation(num1, num2)

def get_user_input():
    operation = input("원하는 연산을 선택해주세요. (addition, subtraction, multiplication, division): ")
    num1 = float(input("첫 번째 숫자를 입력해주세요: "))
    num2 = float(input("두 번째 숫자를 입력해주세요: "))
    return operation, num1, num2

def main():
    operation, num1, num2 = get_user_input()
    if operation == 'addition':
        print(calculator(lambda num1, num2: num1 + num2, num1, num2))
    elif operation == 'subtraction':
        print(calculator(lambda num1, num2: num1 - num2, num1, num2))
    elif operation == 'multiplication':
        print(calculator(lambda num1, num2: num1 * num2, num1, num2))
    elif operation == 'division':
        print(calculator(lambda num1, num2: num1 / num2 if num2 != 0 else "0으로 나눌 수 없습니다.", num1, num2))
    else:
        print("올바른 연산자를 입력해주세요.")

if __name__ == "__main__":
    main()