# - class Arithmetic : 곱셈, 나눗셈 추가
# - 뺄셈 곱셈 나눗셈으로 표시

#class for arithmetics (add minus, multiply, division functions)
class Arithmetics:
    def __init__(self):
        pass
#for input two values
    def get_values(self):
        self.first, self.second = map(int, input("숫자 2개 입력 (공백으로 구분): ").split())

    def add(self):
        sum_result = self.first + self.second
        return sum_result

    def minus(self):
        result = self.first - self.second
        return result

    def multiply(self):
        result = self.first * self.second
        return result

    def division(self):
        result = self.first / self.second
        return result

# class instance
arithmetics = Arithmetics()

# call function
arithmetics.get_values()

# print results
print("뺄셈 : ", arithmetics.minus())
print("곱셈 : ", arithmetics.multiply())
print("나눗셈 : ", arithmetics.division())