def solution(n, lost, reserve):
    answer = n - len(lost)

    for i in lost:
        if i in reserve:
            answer += 1
            del reserve[reserve.index(i)]

        elif i-1 in reserve:
            answer += 1
            del reserve[reserve.index(i-1)]

        elif i+1 in reserve:
            answer += 1
            del reserve[reserve.index(i+1)]

    return answer


n, lost, reserve = 5, [2, 4], [1, 3, 5]

print(solution(n, lost, reserve))