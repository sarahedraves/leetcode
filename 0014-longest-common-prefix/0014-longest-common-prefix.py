class Solution(object):
    def longestCommonPrefix(self, strs):
        minlength=len(min(strs,key=len))
        output=""
        add=True
        for i in range(minlength):
            curletter=strs[0][i]
            for curstr in strs[1:]:
                if curstr[i]!=curletter:
                    add=False
            if add:
                output+=curletter
            else:
                return output
        return output