class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        currentmax=max(candies)
        boolarray=[]

        for num in candies:
            boolarray.append( num+extraCandies>=currentmax)
        
        return boolarray