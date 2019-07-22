# 입력 스트림의 길이가 정의되어있지 않아 5로 가정하겠습니다.
import sys


def main():
    W = int(sys.stdin.readline())

    queue = []
    output = []
    streams = []

    for i in range(5):
        streams.append(int(sys.stdin.readline()))

    for element in streams:
        queue.insert(0, element)

        if len(queue) == W:
            print(max(queue))
            queue.pop()

    return output


main()