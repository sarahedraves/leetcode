class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #brute force complexity O(m*n+n*m)
        answer0=[]
        for value in nums1:
            if value not in answer0 and value not in nums2:
                answer0.append(value)

        answer1=[]
        for value in nums2:
            if value not in answer1 and value not in nums1:
                answer1.append(value)
        
        return [answer0,answer1]