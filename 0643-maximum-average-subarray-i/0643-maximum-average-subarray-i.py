class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # [1,2,3,4,5,6,7]
        # 1, 1 - 1
        # 6, 4 - 3
        # 7, 3 - 5
        # okay so it's length - k + 1 number of possible subarrays
        # so iterate from 0 to length - k

        #brute force method works for shorter arrays but is O(n*k) complexity
        # currentmax=-10**4
        # for i in range(len(nums)-k+1):
        #     currentsum=0
        #     for j in range(k):
        #         currentsum+=nums[i+j]
        #     average=currentsum/k
        #     currentmax=max(currentmax,average)
        # return currentmax

        currentsum=sum(nums[0:k])
        currentmax=currentsum/k
        currentavg=currentmax
        for i in range(k,len(nums)):
            currentavg-=nums[i-k]/k
            currentavg+=nums[i]/k
            currentmax=max(currentavg,currentmax)
        return currentmax