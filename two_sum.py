class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = {}
        for index, value in enumerate(nums):
            ind[value] = index
        for index, value in enumerate(nums):
            if ind.__contains__(target - value) and ind[target - value] != index:
                return index, ind[target - value]