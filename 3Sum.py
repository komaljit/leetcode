def threeSum(self, nums):
    triplets = []
    nums.sort()
    if not nums:
        return []
    prev = nums[0]-1
    for i in range(len(nums)):
        if prev == nums[i]:
            continue
        prev = nums[i]
        l = i+1
        r = len(nums) - 1
        while l < r:
            if nums[i]+nums[l]+nums[r] < 0:
                while l < r and nums[l]==nums[l+1]:
                    l += 1
                l  += 1    
            elif nums[i]+nums[l]+nums[r] > 0:
                while l < r and nums[r]==nums[r-1]:
                    r -= 1
                r -= 1    
            else:
                triplets.append([nums[i], nums[l], nums[r]])
                while l < r and nums[r]==nums[r-1]:
                    r -= 1
                while l < r and nums[l]==nums[l+1]:
                    l += 1
                l += 1
                r -= 1
    return triplets
