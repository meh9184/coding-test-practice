# n개의 배열에서 k번째로 큰 숫자 구하는 프로그램

def solution(L, k):
    for i in range(k):
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

    return L[-k]

L = [2, 6, 4 ,1, 3, 5]

print(solution(L, 5))

