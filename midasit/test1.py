def solution(block, board):
    n = len(board)
    answer = 0
    block_points = [
        [(0, 0), (-1, 0), (-2, 0)],
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (0, 1), (-1, 0)],
        [(0, 0), (0, 1), (-1, 1)],
        [(0, 0), (-1, 0), (-1, -1)],
        [(0, 0), (-1, 0), (-1, 1)]
    ]

    targets = get_targets(board)

    deletion_lines = []
    for target_x, target_y in targets:

        for x, y in block_points[block]:
            if 0 <= target_x + x <= n-1 and 0 <= target_y + y <= n-1:
                board[target_x + x][target_y + y] += 1
        print_board(board)
        print(block_points[block])
        print(count_deletion_lines(board))
        print()

        deletion_lines.append(count_deletion_lines(board))

        for x, y in block_points[block]:
            if 0 <= target_x + x <= n - 1 and 0 <= target_y + y <= n - 1:
                board[target_x + x][target_y + y] -= 1

    answer = max(deletion_lines)

    return answer


def get_targets(board):

    n = len(board)
    targets = []

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                targets.append((x, y))

    return targets


def count_deletion_lines(A):
    count = 0

    for i in range(len(A)):
        if 2 in A[i]:
            return 0
        elif A[i].count(1) == 4:
            count += 1

    return count


def print_board(board):
    for i in range(len(board)):
        print(board[i])


block = 5
board = [
    [1,0,0,0],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,0,1]
]

# board = [
#     [1,0,0,0,0],
#     [1,0,0,1,0],
#     [1,1,0,1,0],
#     [1,1,0,1,0],
#     [0,0,0,0,0]
# ]

print(solution(block, board))
