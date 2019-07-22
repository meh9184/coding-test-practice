def sep_pow_of_bin(n):
	m = 2
	for i in range(1, 18):
		m_ = m ** i
		if n == 1:
			return n, n, 0, 0
		if m_ > n:
			return n, int((m_ - m_ / 2)), int((n - (m_ - m_ / 2))), i - 1


def solution(weights):
	elmt = list(set(weights))
	print(elmt)

	n_elmt = []
	for i in range(len(elmt)):
		n_elmt.append(weights.count(elmt[i]))
	print(n_elmt)

	n_elmt_bin = []
	n_elmt_rsd = []
	n_elmt_info = []
	for j in range(len(n_elmt)):
		_, val, rsd, num_pow = sep_pow_of_bin(n_elmt[j])
		n_elmt_bin.append(val)
		n_elmt_rsd.append(rsd)
		n_elmt_info.append(num_pow)
	print(n_elmt_bin)
	print(n_elmt_rsd)
	print(n_elmt_info)

