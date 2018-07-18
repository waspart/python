# 猴子吃桃问题

#lst = [1] # 记录每天猴子吃了多少个桃子
y = 1
for i in list(range(1,10)):
	y = 2 * (y + 1)

print(y)