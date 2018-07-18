#输出一个菱形
from sys import stdout

ct = 3
for i in list(range(4)):
	for j in list(range(0,7)):
		if j in list(range(ct - i, ct + i + 1)):
			stdout.write('*')
		else:
			stdout.write(' ')
	print()

for i in list(range(2,-1,-1)):
	for j in list(range(0,7)):
		if j in list(range(ct - i, ct + i + 1)):
			stdout.write('*')
		else:
			stdout.write(' ')
	print()

print('\nfinished!')