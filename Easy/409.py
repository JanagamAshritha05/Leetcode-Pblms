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



