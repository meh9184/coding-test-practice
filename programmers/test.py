import sys
import queue

def main():
    # N, C 입력받음
    N, C = sys.stdin.readline().split()

    # Capacity를 C로 하는 queue 생성
    limited_queue = queue.Queue(int(C))

    # 명령 집합
    commands = []

    # N개의 모든 명령을 모음
    for i in range(int(N)):
        commands.append(sys.stdin.readline())

    # 각 명령별로 queue 연산 수행
    for command in commands:
        command = command.split()

        # 큐의 size를 체크하기만 하기 때문에 compelxity는 O(1)이다.
        if command[0] == 'SIZE':
            print(limited_queue.qsize())

        # 큐의 rear를 체크하여 리턴하기 때문에 compelxity는 O(1)이다.
        elif command[0] == 'TAKE':
            if not limited_queue.empty():
                print(limited_queue.get())

        # 큐의 front를 체크하여 리턴하기 때문에 compelxity는 O(1)이다.
        elif command[0] == 'OFFER':
            if not limited_queue.full():
                limited_queue.put(command[1])
                print('true')
            else:
                print('false')

main()