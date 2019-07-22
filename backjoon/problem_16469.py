# 미로 디버그용 출력
def printMaze():
    print('Raw:\t', Raw)
    print('Column:\t', Column)

    print('Player1: ', players[0])
    print('Player2: ', players[1])
    print('Player3: ', players[2])

    print('Maze:\t')
    for i in range(Raw+2):
        for j in range(Column+2):
            print("%2d" % (maze[i][j]), end=' ')
        print()


# 플레이어가 해당 포인트에 방문 했었는지 확인
def isVisited(player, point):
    if player in point:
        return True
    else:
        return False


# 행과 열의 크기 입력받음
Raw, Column = input().split()
Raw, Column = int(Raw), int(Column)

# 미로 입력받음
# maze = [[0 for i in range(R)] for j in range(C)]
maze = list()

maze.append([-1 for i in range(Column+2)])
for i in range(Raw):
    line = [int(i)*-1 for i in input()]
    line.insert(0, -1)
    line.append(-1)
    maze.append(line)
maze.append([-1 for i in range(Column+2)])

# 시작 위치 입력받음
players = list()
players.append([tuple([int(i) for i in input().split()])])
players.append([tuple([int(i) for i in input().split()])])
players.append([tuple([int(i) for i in input().split()])])

# 시작 위치 1 증가
for player in players:
    for point in player:
        maze[point[0]][point[1]] += 1

count = 0


print(players)


