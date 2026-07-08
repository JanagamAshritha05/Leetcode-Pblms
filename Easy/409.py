'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Easy Formula to Remember

Even count (2, 4, 6...) → Use all characters.
Odd count (1, 3, 5...) → Use the largest even part (count - 1).
If there is at least one odd count, add 1 for the center.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.

'''

class Solution:
    def longestPalindrome(self, s: str) -> int:

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        length = 0
        odd = False

        for count in freq.values():

            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd = True

        if odd:
            length += 1

        return length

obj = Solution()
print(obj.longestPalindrome("abccccdd"))

#
class Solution:
    def longestPalindrome(self, s: str) -> int:

        seen = set()
        length = 0

        for ch in s:

            if ch in seen:
                seen.remove(ch)
                length += 2
            else:
                seen.add(ch)

        if seen:
            length += 1

        return length

obj = Solution()
print(obj.longestPalindrome("a"))


# Finding longest Palindrome 
'''
General Algorithm to Build the Palindrome

Step 1

Count the frequency of every character.

Step 2

For every character:

Take as many pairs as possible.
Put half of each pair on the left.
Save one leftover odd character (if any) for the center.
Step 3

Build the palindrome:

Palindrome = Left + Center + Reverse(Left)

example 1: aaaabbccc
a = 4
b = 2
c = 3

Pairs:
from (aa)(aa) -> aa
from (bb) -> b 
from (cc) -> c one c is left right! then move to center 

Left:   center:  Right:

aabc    c        cbaa 

palindrome = aabcccbaa

example 2: s = "abc"

Frequency
a = 1
b = 1
c = 1   No pairs only one character can be the center a or b or c so length = 1

example 3: s = "aaabbb"

Frequency   pairs:  

a = 3       (aa)    left = ab , remaining = a, b center = a , right = ba 
b = 3       (bb)

palindrome = left + center + right = ababa

'''

class Solution():
    def longest_palindrome(self, s:str):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1 
        
        left = ""
        center = ""

        for char in freq:
            left += char*(freq[char]//2) 

            if freq[char]%2==1 and center == "":
                center = char 
        
        right = ""
        for i in range(len(left)-1, -1, -1):
            right += left[i]

        palindrome = left + center + right 

        return palindrome, len(palindrome)


obj = Solution() 
print(obj.longest_palindrome("abccccdd"))




