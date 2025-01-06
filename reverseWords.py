class Solution:
    def reverseWords(self,s:str) -> str:
        words=s.split() #split the string into the list of words
        rev_word=words[::-1] # reversed the string through slicing
        rev_s=' '.join(rev_word) #converts list to string
        return rev_s
    
s=Solution()
print(s.reverseWords('the sky is blue'))