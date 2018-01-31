class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        r = []
        j = 0
        if nums1==[] and nums2== []:
            return None
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                r.append(nums1[i])
                i = i + 1
            elif nums1[i] > nums2[j]:
                r.append(nums2[j])
                j = j + 1
            else:
                r.append(nums1[i])
                r.append(nums2[j])
                i = i + 1
                j = j + 1
        if nums1[i:]:
            r[i + j :] = nums1[i:]
        elif nums2[j:]:
            r[i + j :] = nums2[j:]
        med = len(r) / 2
        if len(r) % 2:
            return r[med]
        return float(r[med] + r[med - 1])/2
