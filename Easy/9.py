class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        else:
            new = ""
            for i in str(x):
                new = i + new 
            
            if new == str(x):
                return True 
            else:
                return False  

object = Solution()
x = -121 
print(object.isPalindrome(x))


        

