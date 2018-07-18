import matplotlib.pyplot as plt

from randomwalk import RandomWalk


while True:
	rw = RandomWalk(1000)
	rw.fill_walk()

	# 设置绘图窗口的尺寸
	plt.figure(dpi=128, figsize=(10, 6))

	point_number = list(range(rw.num_points))

	# plt.scatter(rw.x_val, rw.y_val, c=point_number,\
	# 			cmap=plt.cm.Blues, edgecolor='none', s=1)

	plt.plot(rw.x_val, rw.y_val, linewidth=1)

	# 突出起点和终点
	# plt.scatter(0, 0, c='green', edgecolor='none', s=100)
	# plt.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolor='none', s=100)

	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("Make another walk? (y/n):")
	if keep_running == 'n':
		break

