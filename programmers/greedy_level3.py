def solution(name):
    answer = 0

    ascii_list = []

    for i in name:
        if ord(i) <= 77:
            ascii_list.append(ord(i) - 65)
        else:
            ascii_list.append(26 - (ord(i) - 65))


    for i in range(len(ascii_list)):
        if [0 for i in range(len(ascii_list[i:]))] == ascii_list[i:]:
            break




    print(list(name))
    print(ascii_list)
    print(sum(ascii_list) + len(ascii_list) - 1)

    return answer


name = 'JAN'

print(solution(name))