# 직사각형의 넓이를 계산하기 위해 width와 heigh를 곱하는 연산 1번만을 수행하기 때문에 compelxity는 O(1) 이다.

import sys


def getArea(width, height) -> int:
    # 파라미터로 넘어온 width와 height를 곱하여 return
    return width * height


def main():
    width, height = map(int, sys.stdin.readline().strip().split(' '))
    print(getArea(width, height))


main()