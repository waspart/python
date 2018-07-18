lst = [0, 1]
for i in xrange(2,20):
	x = lst[i - 2] + lst[i - 1]
	lst.append(x)

print lst[1:]
