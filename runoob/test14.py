# -*- coding: UTF-8 -*-
# 因数分解某个给定的正整数

def reduceNum(n):
	print '{} = '.format(n),
	if not isinstance(n, int) or n<=0:
		print u'给定数字有误！'
	elif n == 1:
		print '{}'.format(n)

	while n != 1: #循环保证递归
		for ind in xrange(2, n + 1):
			if n % ind == 0:
				n /= ind
				if n == 1:
					print ind
				else: #此时ind一定是质数
					print '{} * '.format(ind),

				break

reduceNum(111)
reduceNum(100)