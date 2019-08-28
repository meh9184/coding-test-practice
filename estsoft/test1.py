def solution(S):
    # substring "aaa"의 위치를 저장 시킬 list pos_aaa
    pos_aaa = []

    # string S에 존재하는 substring "aaa"의 첫 번째 위치 append
    # 없을 경우 -1 append
    pos_aaa.append(S.find("aaa",0))

    # string S에 substring "aaa"가 존재 할 경우
    if pos_aaa[0] != -1:
        i = 0
        while True:
            # string S에 존재하는 n번째 substring "aaa"의 위치 확인
            idx = S.find("aaa", pos_aaa[i]+1)

            # string S에 존재하는 n번째 substring "aaa"의 위치 append 
            if idx != -1:
                pos_aaa.append(idx)
            # 마지막 substring의 위치일 경우
            else:
                break
            i = i+1
    # string S에 substring "aaa"가 존재 하지 않을 경우
    else:
        pos_aaa = []



    # substring "bbb"의 위치를 저장 시킬 list pos_bbb
    pos_bbb = []

    # string S에 존재하는 substring "bbb"의 첫 번째 위치 append
    # 없을 경우 -1 append
    pos_bbb.append(S.find("bbb",0))

    # string S에 substring "bbb"가 존재 할 경우
    if pos_bbb[0] != -1:
        i = 0
        while True:
            # string S에 존재하는 n번째 substring "bbb"의 위치 확인
            idx = S.find("bbb", pos_bbb[i]+1)

            # string S에 존재하는 n번째 substring "bbb"의 위치 append 
            if idx != -1:
                pos_bbb.append(idx)
            # 마지막 substring의 위치일 경우
            else:
                break
            i = i+1
    # string S에 substring "bbb"가 존재 할 경우
    else:
        pos_bbb = []

    # "aaa" "bbb" 모든 위치 결합 및 정렬
    pos = pos_aaa + pos_bbb
    pos.sort()

    # S에 "aaa" "bbb"가 없을 경우
    if pos == []:
        rst = len(S)
    else:
        # semi-alternating substring들의 길이를 계산
        diffs = []
        # offset: 처음 나오는 "aaa" or "bbb" 까지의 길이 계산
        diffs.append(pos[0]+2)
        for i in range(len(pos)-1):
            diff = pos[i+1]-pos[i]+1
            # 바로 인접해 있는 경우 (e.g., "-aaaa-") 예외 처리: diff <= 2
            if diff > 2:
                diffs.append(diff)
        # longest semi-alternating substring 계산
        rst = max(diffs)

    return rst


S = "abaaabaabbb"

print(solution(S))