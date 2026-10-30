class Solution(object):
    def mySqrt(self, x):
        if x<1:
            return 0
        sqrt=1
        while True:
            if sqrt*sqrt<=x and (sqrt+1)*(sqrt+1)>x:
                return sqrt
            sqrt+=1
        