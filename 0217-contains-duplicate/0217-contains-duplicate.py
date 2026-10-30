class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # duplicate=False
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             duplicate=True
        # return duplicate

        checked=set()
        for num in nums:
            if num in checked:
                return True
            else:
                checked.add(num)
        return False