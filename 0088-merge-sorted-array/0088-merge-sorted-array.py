class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return nums1
        
        nums1copy=nums1[0:m]
        
        write=0
        i=0
        j=0
        for write in range(m+n):
            if j>=n or (i<m and nums1copy[i]<=nums2[j]):
                nums1[write]=nums1copy[i]
                i+=1
            else:
                nums1[write]=nums2[j]
                j+=1

        