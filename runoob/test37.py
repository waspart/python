import sys

# 选择排序法
def selectSort(lst):
	length = len(lst)
	for i in list(range(length)):
		for j in list(range(i + 1, length)):
			if lst[i] > lst[j]:
				lst[i], lst[j] = lst[j], lst[i]
				#t = lst[j]
				#lst[j] = lst[i]
				#lst[i] = t

# 冒泡排序法
def popSort(lst):
 	length = len(lst)
 	for i in list(range(length)):
 		for j in list(range(length - i - 1)):
 			if lst[j] > lst[j + 1]:
 				lst[j], lst[j + 1] = lst[j + 1], lst[j]
 				#t = lst[j]
 				#lst[j] = lst[j + 1]
 				#lst[j + 1] = t

# 在已排序的列表中插入某个数据
def insert(lst, n):
	lst.append(sys.maxsize) #追加最大值，防止插入一个比列表中所有元素都大的值时出错
	length = len(lst)
	ind = 0
	for i in list(range(length)):
		if n >= lst[i]:
			continue
		else:
			ind = i
			break

	for i in list(range(length - 1, ind, -1)):
		lst[i] = lst[i - 1]

	lst[ind] = n

# 追加后直接排序，算法复杂度较高
def anotherinsert(lst, n):
	lst.append(n)
	popSort(lst)


#lst1 = lst2 = lst3 = [98, 34, 22, 15, 88, 54, 9, 67, 72, 43] # 同一个对象的不同引用
lst1 = [98, 34, 22, 15, 88, 54, 9, 67, 72, 43]
lst1.sort()
print(lst1)

lst2 = [98, 34, 22, 15, 88, 54, 9, 67, 72, 43]
selectSort(lst2)
print(lst2)

lst3 = [98, 34, 22, 15, 88, 54, 9, 67, 72, 43]
popSort(lst3)
print(lst3)

s1 = '\\'.join(str(n) for n in lst3)
print(s1)

insert(lst1, 63)
print(lst1)
anotherinsert(lst2, 65)
print(lst2)


