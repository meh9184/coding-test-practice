# 회문 구하는 프로그램

def solution(S):
    for i in range(int(len(S) / 2)):
        if S[i] != S[-(i+1)]:
            return False

    return True


print(solution('abcaa'))