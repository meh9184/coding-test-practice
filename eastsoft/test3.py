def solution(U, L, C):
    
    # C의 크기만큼 0으로 채워진 매트릭스 생성
    M = [
        [0 for _c in range(len(C))],
        [0 for _c in range(len(C))]
    ]

    # C의 값이 2인 경우는, U와 L 모두 1로 채움
    for i, c in enumerate(C):
        if c == 2:
            M[0][i] = 1 
            M[1][i] = 1

            U -= 1
            L -= 1

            # 채워 나가다, U나 L이 0보다 작아진다면 불가능 리턴
            if U < 0 or L < 0:
                return 'IMPOSSIBLE'
                
        if c == 1:
            if U > 0:
                M[0][i] = 1
                U -= 1
            elif L > 0:
                M[1][i] = 1
                L -= 1
            else:
                pass

    
    # U, L 모두 0이라면 성공
    if (U == 0) and (L == 0):
    
        return ''.join(map(str, M[0])) + ',' + ''.join(map(str, M[1]))
        
    else:
        return 'IMPOSSIBLE'


U = 2
L = 2
C = [2, 0, 2, 0]

print(solution(U, L, C))