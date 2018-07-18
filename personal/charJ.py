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
