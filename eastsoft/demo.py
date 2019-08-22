def solution(A):

    values = list(set(A))
    values.sort()

    for i in range(len(values)):
        if i == len(values) - 1:
            if values[i] >= 0:
                return values[i] + 1

        elif (values[i] >= 0) and (values[i+1] - values[i] > 1):
            return values[i] + 1

    return 1



A = [-1, -3, 1]

print(solution(A))