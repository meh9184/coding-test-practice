# # 행과 열의 크기 입력받음
# Raw, Column = 5, 5
#
# # 미로 입력받음
# maze = list()
#
# maze.append([-1 for i in range(Column+2)])
#
# for i in range(Raw):
#     line = [int(i)*-1 for i in input()]
#     line.insert(0, -1)
#     line.append(-1)
#     maze.append(line)
#
# maze.append([-1 for i in range(Column+2)])
#
#
# print('Maze:\t')
# for i in range(Raw + 2):
#     for j in range(Column + 2):
#         print("%2d" % (maze[i][j]), end=' ')
#     print()

def quickSort(x, start, end):
    if start > end:
        return

    pivot = start
    i = pivot + 1
    j = end

    while True:
        while i <= end and x[i] <= x[pivot]:
            i += 1
        while j > start and x[j] >= x[pivot]:
            j -= 1

        if i > j:
            x[j], x[pivot] = x[pivot], x[j]
            break
        else:
            x[i], x[j] = x[j], x[i]

    quickSort(x, start, j-1)
    quickSort(x, j+1, end)


a = [1, 5, 2, 5, 3, 2, 6, 3, 7, 2, 10, 23, 24, 10, 43, 53, 20, 30, 38, 53]

print(a)
quickSort(a, 0, len(a)-1)
print(a)
