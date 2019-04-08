import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    heap = []

    for i in range(1, k):
        stock -= 1

        if i in dates:
            index = dates.index(i)
            heapq.heappush(heap, (-supplies[index], supplies[index]))

        if stock <= 0:
            stock += heapq.heappop(heap)[1]
            answer += 1

        print(i)
        print(stock)
        print(heap)
        print()

    return answer




stock, dates, supplies, k = 4, [4, 10, 15], [20, 5, 10], 30

print(solution(stock, dates, supplies, k))