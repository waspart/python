# 有关字符串的一些测试

name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes!')

if 'a' in name:
    print('Yes!')

if name.find('war') != -1:
    print('Yes!')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
