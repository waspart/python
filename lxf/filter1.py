def is_palindrome(n):
	s = str(n)
	for i in list(range(len(s) // 2)):
		if s[i] != s[len(s) - i - 1]:
			return False
	return True

output = filter(is_palindrome, range(1, 200))
print(list(output))