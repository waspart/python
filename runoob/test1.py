for i in xrange(1,5):
	for j in xrange(1,5):
		for k in xrange(1,5):
			if i != k and i != j and j != k:
				print i * 100 + j * 10 + k