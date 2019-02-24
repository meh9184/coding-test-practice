def solution(clothes):
    answer = 1

    cart = {}

    for i in clothes:

        if cart.get(i[1]) is None:
            cart[i[1]] = list()
            cart[i[1]].append(i[0])
        else:
            cart[i[1]].append(i[0])

    for i in cart:
        answer *= len(cart[i]) + 1

    return answer - 1



clothes = 	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))
