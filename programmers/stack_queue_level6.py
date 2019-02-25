def solution(prices):
    answer = []

    prices.append(10001)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
            elif j == len(prices)-1:
                answer.append(j - i - 1)

    return answer


prices = [498,501,470,489]
print(solution(prices))