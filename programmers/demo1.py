def solution(v):

    x_list = []
    y_list = []

    for [x, y] in v:
        if x not in x_list:
            x_list.append(x)
        else:
            del x_list[x_list.index(x)]

        if y not in y_list:
            y_list.append(y)
        else:
            del y_list[y_list.index(y)]

    return [x_list.pop(), y_list.pop()]

v = [[1, 4], [3, 4], [3, 10]]

print(solution(v))