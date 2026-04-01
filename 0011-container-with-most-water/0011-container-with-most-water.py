class Solution:
    def maxArea(self, height: List[int]) -> int:
        #first do brute force approach
        #nested for loop with O(n^2) complexity
        # maxwater=0
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         curheight=min(height[i],height[j])
        #         curwidth=j-i #this could go negative but obviously that wouldn't affect the max - will fix loop later
        #         maxwater=max(maxwater,curheight*curwidth)
        # return maxwater

        # #okay do a slight improvement of avoiding unnecessary evals
        # maxwater=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)): #cut off unnecessary evals
        #         curheight=min(height[i],height[j])
        #         curwidth=j-i 
        #         maxwater=max(maxwater,curheight*curwidth)
        # return maxwater

        #hmm still not fast enough
        #would sorting help? need to retain indices though
        #would a hashmap/dictionary? could have the keys be the heights
        #insight from hint two that mentions using two points: start with the max width and close the width from there
        #always preserve the index that represents the larger height, because ??
        #if they are the same, just move the right one
        leftindex=0
        rightindex=len(height)-1
        maxwater=rightindex*min(height[leftindex],height[rightindex])
        while leftindex!=rightindex: #exit condition is them equaling each other
            #because then the width would be zero
            curwidth=rightindex-leftindex
            curheight=min(height[leftindex],height[rightindex])
            maxwater=max(maxwater,curwidth*curheight)
            if height[leftindex]>height[rightindex]:
                rightindex-=1
            else:
                leftindex+=1
        
        return maxwater