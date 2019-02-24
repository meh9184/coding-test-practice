# 1000보다 작은 3의 배수와 5의 배수를 모두 합하는 프로그램

def solution(n):
    A = 3 * (int(n / 3) * (int(n / 3) + 1) / 2)
    B = 5 * (int(n / 5) * (int(n / 5) + 1) / 2)
    C = 15 * (int(n / 15) * (int(n / 15) + 1) / 2)

    return int(A+B-C)

print(solution(1000))


