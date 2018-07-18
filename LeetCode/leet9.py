class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        s1 = s[::-1]
        # lst = list(s)
        # lst1 = lst.inverse()
        # print('长度：{}'.format(len(lst) // 2))
        # for i in list(range(len(lst) // 2)):
        # 	lst[i], lst[len(s) - 1 - i] = lst[len(s) - 1 - i], lst[i]
        # print(lst)
        # print(lst1)
        if s1.__eq__(s):
        	return 'true'
        else:
        	return 'false'

if __name__ == '__main__':
	x = int(input())
	s = Solution()
	print(s.isPalindrome(x))