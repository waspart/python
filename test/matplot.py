import matplotlib.pyplot as plt


# sqs = [i*i for i in list(range(6))]
# plt.plot(sqs, linewidth=5)
# plt.title("Square ", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', labelsize=14)


x_vals = list(range(1, 1001))
y_vals = [x**3 for x in x_vals]
plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Reds, edgecolor='none', s=40)
# plt.axis([0, 1100, 0, 1100000])
plt.show()
