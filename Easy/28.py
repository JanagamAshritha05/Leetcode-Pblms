class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

obj = Solution() 
haystack = "sadbutsad"
needle = "sad"
print(obj.strStr(haystack, needle))

# 
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle) + 1):
            match = True 
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    match = False 
                    break 
            if match:
                return i 
        return -1 

obj = Solution() 
haystack = "sadbutsad"
needle = "sad"
print(obj.strStr(haystack, needle))



