import math

def isleap(num):
	for i in xrange(2,int(math.sqrt(num + 1)) + 1):
		if num % i == 0:
			return False
		
	return True


count = 0
for i in xrange(101,201):
	if isleap(i):
		count += 1
		print i

print count


