class Solution(object):
    def gcdOfStrings(self, str1, str2):
        self.str1=str1
        self.str2=str2
        str3=[]

        min_length=min(len(str1),len(str2))
        for i in range(min_length):
            if str1[i] == str2[i]  and str1[i] not in str3:
                str3.append(str1[i])
        # gcd_str=''.join(str3)
        gcd_str=''.join(str3)
        return gcd_str
        
s=Solution()
print(s.gcdOfStrings("ABABAB","AB"))
