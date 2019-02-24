# 피보나치 수열 구하는 프로그램 (재귀 / 반복)

def fibo_recursion(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_recursion(n-2) + fibo_recursion(n-1)


def fibo_interation(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        num1 = 0
        num2 = 1
        num3 = num1 + num2
        for i in range(n-3):
            num1 = num2
            num2 = num3
            num3 = num1 + num2

        return num3


n = 50
print(fibo_interation(n))
print(fibo_recursion(n))

