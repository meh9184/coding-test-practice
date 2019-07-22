def solution(priorities, location):
    answer = 0

    queue = []
    sortedList = priorities[:]
    sortedList.sort()

    for index, value in enumerate(priorities):
        queue.insert(0, [index, value])

    while len(queue) is not 0:
        element = queue.pop()
        if element[1] < sortedList[-1]:
            queue.insert(0, element)
        else:
            answer += 1
            sortedList.pop()
            if element[0] == location:
                break

    return answer


priorities, location = [1, 1, 9, 1, 1, 1], 0

print(solution(priorities, location))