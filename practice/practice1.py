# 팬케이크 정렬하는 프로그램

def pancakeSort(P):
    for i in range(len(P)-1):
        maxIndex = findMaxIndex(P) if i is 0 else findMaxIndex(P[:-i])
        flip(P, maxIndex)
        flip(P, len(P) - (i+1))
        print(P)


def findMaxIndex(P):
    maxIndex = 0
    for i in range(1, len(P)):
        if P[maxIndex] < P[i]:
            maxIndex = i

    return maxIndex


def flip(P, index):
    tmp = P[:index+1]
    tmp.reverse()
    P[:index+1] = tmp


P = [1, 3, 2, 4, 5, 8, 6]

pancakeSort(P)
