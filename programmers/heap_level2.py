def solution(stock, dates, supplies, k):
    answer = 0

    for i in range(len(dates)):

        if i != 0:
            stock -= (dates[i]-dates[i-1])
        else:
            stock -= dates[i]

        remains = k - dates[i]
        all_supplies = sum(supply for supply in supplies[i+1:])
        if stock - remains + all_supplies < 0:
            stock += supplies[i]
            answer += 1

        print(stock)

    return answer

stock, dates, supplies, k = 4, [4, 10, 15], [20, 5, 10], 30

print(solution(stock, dates, supplies, k))