class Solution:
    def reverseVowels(self, s: str) -> str:
        reverse=[]
        i=0
        vowel=[]
        vowels='aeiouAEIOU'
        for char in s:
            if char in vowels:
                vowel.append(char)
        vowel.reverse()
        for char in s:
            if char in vowels:
                reverse.append(vowel[i])
                i+=1
            else:
                reverse.append(char)
        rev_str=''.join(reverse)
        return rev_str

s=Solution()
print(s.reverseVowels("leetcode"))