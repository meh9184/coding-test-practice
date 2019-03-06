def main():
    _queue = []

    N = int(input())
    _status = [0] * N
    _hash = {}

    for i in range(N):
        s, g = map(int, input().strip().split(' '))

        if s in _hash:
            _hash[s].append(g)
        else:
            _hash[s] = [g]

    while _hash:

        (key, values) = _hash.popitem()

        for _value in values:
            _queue.append(_value)

        _status[key] = 1

        while _queue:
            _node = _queue.pop(0)

            if _status[_node]:
                print("true")
                exit()
            _status[_node] = 1

            if _node in _hash:
                for _value in _hash.pop(_node):
                    _queue.append(_value)

    print("false")


main()