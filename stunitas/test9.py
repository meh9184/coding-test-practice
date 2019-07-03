# 값 입력 받음
N = int(input())
maze = [list(map(int, list(input()))) for _ in range(N)]

dist = [[0]*N for _ in range(N)]
dn = [0, 0, 1, -1]
dm = [1, -1, 0, 0]


queue = list()

queue.append([0, 0])
dist[0][0] = 1

while queue:
    n, m = queue.pop(0)

    if n == N - 1 and m == N - 1:
        print(dist[n][m]-1)
        break

    for i in range(4):
        _n = n + dn[i]
        _m = m + dm[i]

        if 0 <= _n < N and 0 <= _m < N:
            if dist[_n][_m] == 0 and maze[_n][_m] == 1:
                dist[_n][_m] = dist[n][m] + 1
                queue.append([_n, _m])
