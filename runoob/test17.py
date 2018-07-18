#-*-coding:UTF-8-*-


import string

str = input('input a string: ')

ln = 0
dn = 0
sn = 0
on = 0

for s in str:
	if s.isalpha():
		ln += 1
	elif s.isdigit():
		dn += 1
	elif s.isspace():
		sn += 1
	else:
		on += 1

print('letter='+ln+', digit='+dn+', space='+sn+', others'+on)
	