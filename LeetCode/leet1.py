class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind1 = -1
        ind2 = -1
        # print(list(range(len(nums))))
        for i in list(range(len(nums))):
        	ano = target - nums[i]
        	if ano in nums[i + 1:]:
        		ind1 = i
        		ind2 = nums[i + 1:].index(ano) + i + 1
        		break
        return [ind1, ind2]

if __name__ == '__main__':
	str_in = input()
	nums = [int(n) for n in str_in[1:-1].split(',')]
	# nums = list(str_in)
	# print(nums)
	target = int(input())
	s = Solution()
	print(s.twoSum(nums, target))