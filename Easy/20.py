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


