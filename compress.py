class Solution:
    def compress(self,chars:list[str])-> int:
        s={}
        for char in chars:
            s[char]=s.get(char,0)+1
        result = [str(item) for pair in s.items() for item in pair]
        n=len(result)
        return (f"Return {n}, and the first {n} characters of the input array should be: {result}")
s=Solution()
print(s.compress(["a","a","b","b","b"]))
# n=len(lst)
# print(f"Return {n}, and the first {n} characters of the input array should be: {lst}")
