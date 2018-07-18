a = 1
b = 2
s = 0

for i in list(range(1,21)):
	s += b / a
	t = a
	a = b
	b = b + t

print(s)