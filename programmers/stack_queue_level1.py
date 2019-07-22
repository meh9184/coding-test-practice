def solution(arrangement):
    answer = 0

    stack = []

    for i in range(len(arrangement)):
        if arrangement[i] is '(':
            stack.append(arrangement[i])
        elif arrangement[i] is ')' and i != 0:
            if arrangement[i-1] == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1

    return answer

arrangement = "()(((()())(())()))(())"

print(solution(arrangement))