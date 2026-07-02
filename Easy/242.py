#Valid anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True 
        else:
            return False 
        
obj = Solution()
s = "ana"
t = "naa"
print(obj.isAnagram(s, t))

#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        else:
            freq1 = {}
            freq2 = {}
            for i in range(len(s)):
                freq1[s[i]] = freq1.get(s[i], 0) + 1
                freq2[t[i]] = freq2.get(t[i], 0) + 1

            return freq1 == freq2 

obj = Solution()
s= "a"
t = "ab"
print(obj.isAnagram(s, t))

#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        else:
            freq = {}
            for i in range(len(s)):
                freq[s[i]] = freq.get(s[i], 0) + 1
                
            for char in t:
                if char not in freq:
                    return False 
                freq[char] -= 1
                
            for value in freq.values():
                if value != 0:
                    return False 
                
            return True 
            

obj = Solution()
s= "a"
t = "ab"
print(obj.isAnagram(s, t))





