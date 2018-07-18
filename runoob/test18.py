import math

num = int(input('输入数字：'))
n = int(input('输入个数：'))
#print(isinstance(n, int))

sums = 0

for i in list(range(n)):
	if i == 0:
		x = num
	else:
	    x = num * (10 ** i) + x
	sums += x

print(sums)
