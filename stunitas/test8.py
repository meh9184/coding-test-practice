def min_jump_i(M, i):
    min = M[0]
    if i == 0:
        min = M[1]

    for j in range(len(M)):
        if i != j and M[j] < min:
            min = M[j]

    return min


N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

dists = []

i = 0
dist = 0
for _ in range(N):
    visit = [i]

    dist_min = min_jump_i(M[i], i)

    for j in range(N):
        if (i != j) and (M[i][j] == dist_min) and (j not in visit):
            dist += M[i][j]
            visit.append(j)
            i = j
            break

    # print(visit)
    # print(dist)