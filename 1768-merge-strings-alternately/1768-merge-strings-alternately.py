class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #determine longer string
        longer=0
        length=0
        if len(word1)>len(word2):
            longer=1
            length=len(word2)
        elif len(word1)<len(word2):
            longer=2
            length=len(word1)
        else: #they are equal
            length=len(word1)
        
        word=''
        for i in range(length):
            word+=word1[i]+word2[i]
        
        if longer==1:
            word+=word1[length:]
        elif longer==2:
            word+=word2[length:]

        return word