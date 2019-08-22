def solution(N):
    # write your code in Python 3.6

    prev_position = 0
    diff = 0

    base, position = get_boudary(N)

    while N - base > 0:
        
        N -= base
        prev_position = position

        base, position = get_boudary(N)
        
        if diff < prev_position - position:
            diff = prev_position - position -1

    return diff
    

def get_boudary(N):
    base = 1
    position = 0

    while N-(base*2) >= 0:
        base *= 2
        position += 1

    return base, position

print(solution(1345601))