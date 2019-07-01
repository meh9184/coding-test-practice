# def fivo(n):
#     if n <= 0:
#         return 0
#     elif n <= 2:
#         return 1
#     else:
#         return fivo(n-2) + fivo(n-1)
#
# print(fivo(int(input())))

n  = int(input())

su1 = 0
su2 = 1
su3 = 0

if n <= 0:
    print(0)
elif n <= 1:
    print(1)
else:
    for i in range(n):
        su1 = su2
        su2 = su3
        su3 = su1 + su2

    print(su3)
