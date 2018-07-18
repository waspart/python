# -*- coding: UTF-8 -*-
#打印水仙花数

for i in xrange(100,1000):
	x1 = i / 100
	x2 = (i - 100 * x1) / 10
	x3 = i % 10
	if x1 ** 3 + x2 ** 3 + x3 ** 3 == i:
		print i