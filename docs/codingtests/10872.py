# 문제
## 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
## 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
## 첫째 줄에 N!을 출력한다.

# 백준 제출용
# class Fcalculator:
#     def __init__(self, n):
#         self.n = n
#     def factorial(self):
#         if self.n == 0 or self.n == 1:
#             return 1
#         else:
#             return self.n * Fcalculator(self.n-1).factorial()  
# number = int(input())
# calculator = Fcalculator(number)
# result = calculator.factorial()
# print ("{}".format(result))

class Fcalculator:
    def __init__(self, n):
        self.n = n
    def factorial(self):
        if self.n == 0 or self.n == 1:
            return 1
        else:
            return self.n * Fcalculator(self.n-1).factorial()  
number = int(input("계산하고 싶은 숫자를 입력해 주세요: "))
calculator = Fcalculator(number)
result = calculator.factorial()
print ("{}! = {}".format(number,result))





        

        