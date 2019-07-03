test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    velocities = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    while True:
        velocity_min = min(velocities)
        tmp = 0

        for i, velocity in enumerate(velocities):
            if velocity == velocity_min:
                velocities[i] += 1
                tmp += costs[i]

        if M-tmp < 0:
            print(velocity_min)
            break
        else:
            M -= tmp

        print(velocities, M)
