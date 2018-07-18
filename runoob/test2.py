# -*- coding: UTF-8 -*-

i = int(raw_input('liry:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0.0
for ind in xrange(1,6):
	if i > arr[ind]:
		r += (i - arr[ind]) * rate[ind]
		print (i - arr[ind]) * rate[ind]
		i = arr[ind]
print r