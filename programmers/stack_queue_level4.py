import math

def solution(progresses, speeds):
    answer = []
    start = 0

    remains = []
    group = []

    for progress, speed in zip(progresses, speeds):
        remains.append(math.ceil((100-progress) / speed))

    remains.append(-1)

    for i in range(len(remains)):
        if remains[i] > remains[start] or remains[i] == -1:
            answer.append(i-start)
            start = i

    return answer


progresses, speeds = [93, 30, 55], [1, 30, 5]

print(solution(progresses, speeds))