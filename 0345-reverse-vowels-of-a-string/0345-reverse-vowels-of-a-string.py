class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        letters=list(s) #convert to list for item assignment
        toreplace=[] #use list as a stack with last in first out structure
        for index,letter in enumerate(letters):
            if letter in vowels:
                toreplace.append(letter) 
        for index,letter in enumerate(letters):
            if letter in vowels:
                letters[index]=toreplace.pop()
        return ''.join(letters) #convert back to string