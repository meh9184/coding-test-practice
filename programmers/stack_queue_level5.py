def solution(heights):
    answer = []

    heights.insert(0, 101)

    for i in range(len(heights)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer.insert(0, j)
                break

    return answer


heights = [3, 9, 9, 3, 5, 7, 2]
print(solution(heights))