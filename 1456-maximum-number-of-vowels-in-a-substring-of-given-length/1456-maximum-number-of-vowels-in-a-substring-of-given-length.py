class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #iterate through all the letters in the string, cutting off early to prevent indexing letters that don't exist
        #store all the possible substrings in a list
        #iterate through all the substrings and count number of vowels
        #put those numbers in another list
        #return the max

        # substrings=[]
        # for i in range(len(s)-k+1): #O(n)
        #     substrings.append(s[i:i+k]) #O(1)
        
        # vowels='aeiou'
        # numvowels=[]
        # for substring in substrings: O(n*k*5)
        #     count=0
        #     for letter in substring:
        #         if letter in vowels:
        #             count+=1
        #     numvowels.append(count) #O(1)

        # return max(numvowels) #O(n)

        #minimize storage
        # vowels='aeiou'
        # maxvowels=0
        # for i in range(len(s)-k+1): #O(n)
        #     substring=s[i:i+k] #O(1)
        #     count=0
        #     for letter in substring:
        #         if letter in vowels:
        #             count+=1
        #     maxvowels=max(maxvowels,count) #O(1)

        # return maxvowels 

        #minimize time
        vowels='aeiou'
        firststr=s[:k]
        curvowels=0
        for letter in firststr:
            if letter in vowels:
                curvowels+=1
        maxvowels=curvowels

        for i in range(1,len(s)-k+1): #O(n)
            lostletter=s[i-1]
            gainedletter=s[i+k-1]
            if lostletter in vowels:
                curvowels-=1
            if gainedletter in vowels:
                curvowels+=1
            maxvowels=max(maxvowels,curvowels) 

        return maxvowels 