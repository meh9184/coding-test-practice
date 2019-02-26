def solution(number, k):
    answer = ''

    for i in range(len(number)-k-1, -1, -1):
        if i == 0:
            answer += max(number)
        else:
            answer += max(number[:-i])
            number = number[number.index(max(number[:-i]))+1:]



    return answer


number, k = "4177252841", 4

print(solution(number, k))