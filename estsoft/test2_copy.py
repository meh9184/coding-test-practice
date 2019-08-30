# from extratypes import Tree

class Tree(object):
    def __init__(self, value):
        self.x = value

    l = None
    r = None

def solution(T):

    if T == None:
        return 0
    
    # 중복된 값을 담아놓을 해시
    distinct_values = dict()

    return get_longest_distinct_path(T, distinct_values)
    

# 트리를 루트노드부터 리프노드까지 내려가며 최장 길이 longest_distinct_path를 계산
def get_longest_distinct_path(T, distinct_values):

    ### 수정된 부분 ###
    # 만약 노드의 값이 없거나, 중간에 중복된 값이 발생했을 경우 현재 해시 크기를 반환
    if (T == None) or (T.x in distinct_values.keys()):
        return len(distinct_values)

    else:
        ### 수정된 부분 ###
        # 해시에 현재 노드의 값을 삽입
        distinct_values[T.x] = 1

        # 좌우 서브 트리의 longest_distinct_path 값을 계산하여 (분할정복) 큰 값을 반환
        max_path = max(get_longest_distinct_path(T.l, distinct_values), 
                       get_longest_distinct_path(T.r, distinct_values))

        ### 수정된 부분 ###
        # 해당 노드의 키값을 추가하여 연산이 끝났다면, 해시에서 다시 삭제
        del distinct_values[T.x]

        return max_path; 



T = Tree(1)
T.l = Tree(2)
T.r = Tree(3)

T.l.l = Tree(3)
T.l.r = Tree(6)

T.r.l = Tree(3)
T.r.r = Tree(1)

T.l.l.l = Tree(2)

T.r.r.l = Tree(5)
T.r.r.r = Tree(6)



print(solution(T))