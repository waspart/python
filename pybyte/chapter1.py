age = 20
name = 'Nick'
height = 173.5
print('\n{0} was {1} years old and ajali '.format(name, age))
print('height : {0:.3f}'.format(height))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用^定义“___hello___”字符串长度为11
print('{0:_^11}'.format('hello'))

#基于关键词输出
print('{name} wrote {book}'.format(name='Swarop', book='A Byte of Python'))

# end可以避免print语句默认换行
print('abc', end=' ')
print('defg', end='')

# 反斜杠'\'表示字符串在下一行继续
s = 'this is the first sentence. \
this is the second sentence.'
print(s)


print(r'Newline is indicated by \n')

print()