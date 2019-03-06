import sys

def main():
    sticks = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    num = len(sticks)
    rst = []
    for x in range(num):
        for delta in range(num-(x+1)):
            if sticks[x] + sticks[x+(delta+1)] == target:
                print(sticks[x], sticks[x+(delta+1)])
                return

    print(-1)

main()

