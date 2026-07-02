class Solution():
    def isPalindrome(self, s:str):
        s = s.lower()
        new = ""
        for char in s:
            if char.isalnum():
                new += char 
        
        rev = "" 
        for i in range(len(new)-1, -1, -1):
            rev += new[i]
        
        return rev == new


obj = Solution() 
s = "A man, a plan, a canal: Panama" 
print(obj.isPalindrome(s))


#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz0123456789':
                new += char 

        return new == new[::-1]
    
obj = Solution()
print(obj.isPalindrome("madam"))

#
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():  
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True     #If the loop finishes without finding any mismatch, it means every character matched.
        
        
obj = Solution() 
s = "Madam"
print(obj.isPalindrome(s))








        
        
        





