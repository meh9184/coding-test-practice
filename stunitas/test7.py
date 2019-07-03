n = int(input())
numbers = list(map(int, input().split()))

results = [1]

for i in range(2, n+1):
    results.insert(numbers[i-1], i)

while results:
    print(results.pop(), end=' ')
