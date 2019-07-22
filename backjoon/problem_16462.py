import math

# 학생 수 N 입력받음
N = int(input())

# N개의 성적 입력받음
scores = list()
for i in range(N):
    scores.append(int(input()))

for i in range(len(scores)):
    if scores[i] > 10 and int(scores[i] / 10) % 6 == 0:
        scores[i] += 30

    if scores[i] % 10 == 0:
        scores[i] += 9
    elif scores[i] % 6 == 0:
        scores[i] += 3

    if scores[i] > 100:
        scores[i] = 100

avg = sum(scores, 0.0) / len(scores)

if int(str(avg)[str(avg).find('.')+1:str(avg).find('.')+2]) >= 5:
    avg = math.ceil(avg)
else:
    avg = math.floor(avg)

print(avg)