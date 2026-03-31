class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i=0
        # list_t=list(t)
        # while i<len(list_t):
        #     if list_t[i] not in s:
        #         list_t.pop(i)
        #     else:
        #         i+=1
        # string=''.join(list_t)
        # print(string)
        # #return s==string - misses "ab" in "baab" b/c they don't equal
        # return s in string #misses situations where the final string has an extra duplicate letter compared to the subsequence

        #recursive version
        #check two possible base cases
        if len(s)==0:
            return True #because all the subsequence letters have been matched 
        elif len(t)==0:
            return False #because we have used up all the target letters without matching all the subsequence letters
        
        #what to do if not in base case
        if s[0]==t[0]: #when first letters match
            return self.isSubsequence(s[1:],t[1:]) #then check if the rest of the subsequence is in the rest of the target
        else:
            return self.isSubsequence(s,t[1:]) #knock the unmatching letter of target and keep searching