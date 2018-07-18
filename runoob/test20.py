# 一个球从100m高度落下

height = [100]
h = height[0]
for i in list(range(1,10)):
	h = h / 2
	height.append(h)

#print(height)
print('第十次弹起高度为：' + repr(height[9]))

tour = sum(height) + sum(height[1:])
print('第十次落地时，该球所经历的长度：' + repr(tour))
