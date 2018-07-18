def check_is_chinese(check_char):
	'''判定一个字符是否属于中文'''
	if u'\u4e00' <= check_char <= u'\u9fff':
		return True

def ext_chinese(check_str):
	'''提取一个字符串中所有中文字符，丢弃其他字符'''
	res = ''
	for ch in check_str:
		if u'\u4e00' <= ch <= u'\u9fff':
			res = res + ch

	return res

def ext_non_char(check_str):
	'''去除字符串中所有英文字符以及空格'''
	res = ''
	for ch in check_str:
		if 'a' <= ch <= 'z' \
				or 'A' <= ch <= 'Z' \
				or ch == ' ':
			continue
		else:
			res += ch

	return res


# check_str = '小明说：“39个人刚刚过去了，i am the last!'
# print(ext_non_char(check_str))
