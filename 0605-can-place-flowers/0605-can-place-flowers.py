class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newflowers=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0: #only check if there's no flowers there to begin with
                adjacent=0
                #check left
                if i!=0:
                    adjacent+=flowerbed[i-1]
                #check right
                if i!=len(flowerbed)-1:
                    adjacent+=flowerbed[i+1]
                if adjacent==0:
                    newflowers+=1
                    flowerbed[i]=1 #plant new flower so ones to the right evaluate correctly
        return newflowers>=n