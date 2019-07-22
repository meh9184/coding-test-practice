def solution(S, K):

    _str = S
    _arr = S.split(" ")

    _stack = []

    for _i, _v in enumerate(_arr):
        if len(_v) > K:
            return -1
        elif len(_stack) > 0:
            _pop = _stack.pop()
            if len(_pop) + len(_v) + 1 <= K:
                _stack.append(_pop+" "+_v)
            else:
                _stack.append(_pop)
                _stack.append(_v)

        else:
            _stack.append(_v)

    return len(_stack)

