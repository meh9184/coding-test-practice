def solution(S):
    
    pos_aaa = []
    pos_aaa.append(S.find("aaa",0))

    if pos_aaa[0] != -1:
        i = 0
        while True:
            idx = S.find("aaa", pos_aaa[i]+1)

            if idx != -1:
                pos_aaa.append(idx)
            else:
                break
            i = i+1
    else:
        pos_aaa = []

    
    pos_bbb = []

    pos_bbb.append(S.find("bbb",0))

    if pos_bbb[0] != -1:
        i = 0
        while True:
            idx = S.find("bbb", pos_bbb[i]+1)

            if idx != -1:
                pos_bbb.append(idx)
            else:
                break
            i = i+1
    else:
        pos_bbb = []

    pos = pos_aaa + pos_bbb
    pos.sort()

    if pos == []:
        rst = len(S)
    else:
        diffs = []
        diffs.append(pos[0]+2)
        for i in range(len(pos)-1):
            diff = pos[i+1]-pos[i]+1
            if diff > 2:
                diffs.append(diff)

        ### 추가된 부분 ###
        diffs.append(len(S) - pos[-1] - 1)

        rst = max(diffs)

    return rst


S = "aaba"

print(solution(S))