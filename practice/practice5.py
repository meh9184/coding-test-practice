# 10진수를 8진수로 바꾸는 프로그램

def solution(n):
    result = ""

    while n >= 8:
        result = str(n % 8) + result
        n = int(n / 8)

    return int(str(n) + result)

print(solution(17))