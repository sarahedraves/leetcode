class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentalt=0
        maxalt=0
        for currentgain in gain:
            currentalt+=currentgain
            maxalt=max(maxalt,currentalt)
        return maxalt