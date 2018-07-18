# 找出1000以内的“完数”，即其所有因子（非因式分解，不计重复）之和等于其自身

def iscompl(num):
	lst = [num]
	if not isinstance(num, int):
		print('所给数字有误！')
		return
	for ind in list(range(1, int(num / 2) + 1)):
		if num % ind == 0:
			lst.append(ind)

	if lst[0] == (sum(lst[1:])):
		return True
	else:
		return False
	

count = 0
for i in list(range(2,10001)):
	if iscompl(i):
		print(i)
		count += 1

print(count)


