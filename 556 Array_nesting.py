class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lar_nested_len = 0
        for i in range(len(nums)):
            lar_nested_len = max(lar_nested_len, self.array_nesting_helper(i, nums))
        return lar_nested_len

    def array_nesting_helper(self, index, nums):
        index_set = set()
        while index not in index_set:
            index_set.add(index)
            index = nums[index]
        return len(index_set)
