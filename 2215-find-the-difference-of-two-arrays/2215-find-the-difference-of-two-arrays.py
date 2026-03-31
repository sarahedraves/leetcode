class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #brute force complexity O(m*n+n*m)
        # answer0=[]
        # for value in nums1:
        #     if value not in answer0 and value not in nums2: #in commands are essentially doing a nested loop because they are checking lists
        #         #also had to check if in answer0 to avoid duplicates
        #         answer0.append(value)

        # answer1=[]
        # for value in nums2:
        #     if value not in answer1 and value not in nums1:
        #         answer1.append(value)
        
        # return [answer0,answer1]

        #hash set approach
        #building the sets is O(n)
        set1=set(nums1) #this will remove duplicates but that is good
        set2=set(nums2)

        #now iterate through each array once
        answer0=[] #okay to use a list for this because appending to a list is O(1) in Python
        for value in set1: #iterate through sets not lists to avoid duplicates
            if value not in set2: #this is O(1) because it's checking a set
                answer0.append(value)

        answer1=[]
        for value in set2:
            if value not in set1:
                answer1.append(value)
        
        return [answer0,answer1]