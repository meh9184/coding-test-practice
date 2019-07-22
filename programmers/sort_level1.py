def solution(array, commands):
    answer = []

    for command in commands:
        tmp = array[command[0] - 1:command[1]]
        tmp.sort()
        answer.append(tmp[command[2]-1])

    return answer


array, commands = 	[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))