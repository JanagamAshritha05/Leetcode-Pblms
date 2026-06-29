class Solution:
    def lengthOfLastword(self, s:str):
        res = s.split() 
        return len(res[-1])
    

s = "Hello World" 
obj = Solution() 
print(obj.lengthOfLastword(s))

#
class Solution():
    
    def lengthOfLastWord(self, s: str) -> int:
        count = 0 
        last = 0
        for char in s:
            if char != " ":
                count += 1 
                last = count 
            else:
                count = 0 

        return last 
        
    

s = "Hello I am Python!"
obj = Solution() 
print(obj.lengthOfLastWord(s))

#
class Solution():
    
    def lengthOfLastWord(self, s: str) -> int:
        count = 0 
        last = 0
        
        i = 0 
        while i<len(s):
            if s[i]!=" ":
                count += 1 
                last = count 
            else:
                count = 0 
            i+=1 

        return last 
    

s = "Hello I am Python"
obj = Solution() 
print(obj.lengthOfLastWord(s))




