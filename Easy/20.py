class Solution:
    def isValid(self, s: str):
        pairs = ["()", "[]", "{}"]
        
        while True:
            Found_pair = False 
            for pair in pairs:
                if pair in s:
                    s = s.replace(pair, "")
                    Found_pair = True 

            if not Found_pair:
                break 

        return len(s)==0

        
obj = Solution() 
s = "()[]{}"
print(obj.isValid(s))

##
class Solution:
    def isValid(self, s:str):
        stack = []
        brackets = {")":"(", "}": "{", "]":"["}

        for char in s:
            if char in brackets: #we are checking with keys
                if stack and stack[-1] == brackets[char]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
    

obj = Solution() 
s = "()[]{}"
print(obj.isValid(s))


