class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #must be equal for as long as the shorter string is
        length=min(len(str1),len(str2))
        for i in range(length):
            if str1[i]!=str2[i]:
                return ''

        #find numerical GCF which should be length of substring
        a=len(str1)
        b=len(str2)
        if b>a:
            a,b=b,a
        while b:
            a,b=b,a%b
        factorlen=a

        guess=str1[:factorlen]
        if str1!=guess*(len(str1)//factorlen) or str2!=guess*(len(str2)//factorlen):
            return ''
        return guess