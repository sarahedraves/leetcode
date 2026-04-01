class Solution:
    def removeStars(self, s: str) -> str:
        #just use a stack
        letters=[]
        for letter in s:
            if letter=='*':
                letters.pop()
            else:
                letters.append(letter)
        return ''.join(letters)