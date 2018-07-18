for i in xrange(1,85):
	if 168 % i == 0:
		j = 168 / i
		if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
			m = i + j
			n = i - j
			x = n * n - 100
			print x, m, n