def cols(matrix, i):
    return [row[i] for row in matrix]


def solution(A):

    if len(A) <= 2:
        return 0
    elif len(cols(A, 0)) <= 2:
        return 0

    # num_row
    N = len(A)
    # num_col
    M = len(A[0])

    count = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if (A[i][j] == max(cols(A, j)[1:M - 1])) and (A[i][j] == min(A[i][1:N - 1])):
                count = count + 1

            elif (A[i][j] == min(cols(A, j)[1:M - 1])) and (A[i][j] == max(A[i][1:N - 1])):
                count = count + 1

    return count


A = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]

print(solution(A))