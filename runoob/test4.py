year = int(raw_input('year: '))
month = int(raw_input('month: '))
day = int(raw_input('day: '))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def run(year):
	if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
		return True
	else:
		return False

if run(year) and month > 2:
	print 'leap year'
	print day + 1 + sum(days[0 : month - 1])
else:
	print 'not leap year'
	print day + sum(days[0 : month - 1])
