class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for index,value in enumerate(nums):
        #     if value==0:
        #         nums.pop(index)
        #         nums.append(0)

        #alt version without using append
        numzeros=0
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                numzeros+=1
            else:
                i+=1
        nums.extend([0]*numzeros)