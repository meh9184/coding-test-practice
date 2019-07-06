def solution(s, t):

	if len(s) % len(t) == 0 or len(t) % len(s) == 0:

		if len(s) >= len(t):

			rep = len(s) // len(t)

			for i in range(rep):

				if s[len(t) * i:len(t) * (i + 1)] != t:

					answer = False
					break

				answer = True

		else:

			rep = len(t) // len(s)

			for i in range(rep):

				if t[len(s) * i:len(s) * (i + 1)] != s:

					answer = False
					break

				answer = True


	else:
		answer = False

	return answer