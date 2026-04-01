class Solution:
    def reverseWords(self, s: str) -> str:
        #outline:
        #iterate through all characters in string 
        #add words as they are found to a list
            #identify words by having a string called curword 
            #if you hit a space, add curword to the list if it's not '' and reset curword to ''
            #if you hit a letter, append it to curword
        #iterate through the words list backward
        #add each word to a string with a space
        #return everything except the extra space put at the beginning

        words=[]
        curword=''
        for curletter in s: #O(n)
            if curletter==' ':
                if curword!='':
                    words.append(curword) #O(1)
                    curword=''
            else:
                #curword+=curletter
                curword=''.join([curword,curletter]) #more efficient string join
        #need to add the last word if there were no spaces at the end
        if curword!='':
            words.append(curword)
        
        #print(words) #check that we're separating words correctly

        newstring=''
        for word in reversed(words): #also O(n)
            newstring=''.join([newstring,word,' '])
        return newstring[:-1] #chop off the extraneous space

