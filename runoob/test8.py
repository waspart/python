# -*- coding: UTF-8 -*-
#输出九九乘法表
for i in xrange(1,10):
	for j in xrange(1, i + 1):
		print '%d*%d=%d' % (i, j, i*j)

	print