# First Unique Character 
# Frequency Count(Hash Map)
'''
==========================================================
LeetCode 387 - First Unique Character in a String
Pattern: Frequency Count (Hash Map / Dictionary)

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

==========================================================

ALGORITHM

1. Create an empty dictionary called freq.
2. Traverse the string and count the frequency of each character.
3. Traverse the string again from left to right.
4. If the frequency of the current character is 1,
      return its index.
5. If no unique character is found,
      return -1.

----------------------------------------------------------

PSEUDO CODE

freq = {}

for each character in s:

      freq[character]++

for i from 0 to length of s - 1:

      if freq[s[i]] == 1:

            return i

return -1

----------------------------------------------------------

DRY RUN

Input

s = "loveleetcode"


Step 1 : Build Frequency Dictionary

l → 2
o → 2
v → 1
e → 4
t → 1
c → 1
d → 1

Frequency Dictionary

{
l:2,
o:2,
v:1,
e:4,
t:1,
c:1,
d:1
}

----------------------------------------------------------

Step 2 : Traverse Again

Index = 0

Character = l

Frequency = 2

Not unique

Move next

----------------------------------------------------------

Index = 1

Character = o

Frequency = 2

Not unique

Move next

----------------------------------------------------------

Index = 2

Character = v

Frequency = 1

Unique Character Found

Return 2

----------------------------------------------------------

Output

2


Time Complexity : O(n)

Space Complexity : O(k)

(k = Number of unique characters.
For lowercase English letters, k ≤ 26, so it is often considered O(1).)

'''
# Frequency Count(Array)
'''

ALGORITHM

1. Create a frequency array of size 26 with all values as 0.
2. Traverse the string.
3. Convert each character into an array index.
4. Increase its frequency.
5. Traverse the string again.
6. Convert the current character into an index.
7. If its frequency is 1, return the current index.
8. If no unique character is found, return -1.

----------------------------------------------------------

PYTHON PSEUDO CODE

freq = [0] * 26

# Count frequency
for ch in s:

      index = ord(ch) - ord('a')

      freq[index] += 1


# Find first unique character
for i in range(len(s)):

      index = ord(s[i]) - ord('a')

      if freq[index] == 1:

            return i

return -1

----------------------------------------------------------

DRY RUN

Input

s = "loveleetcode"

----------------------------------------------------------

Step 1

freq = [0] * 26

----------------------------------------------------------

Read 'l'

index = ord('l') - ord('a')

108 - 97 = 11

freq[11] += 1

----------------------------------------------------------

Read 'o'

index = ord('o') - ord('a')

111 - 97 = 14

freq[14] += 1

----------------------------------------------------------

Read 'v'

index = ord('v') - ord('a')

118 - 97 = 21

freq[21] += 1

----------------------------------------------------------

Read 'e'

index = ord('e') - ord('a')

101 - 97 = 4

freq[4] += 1

----------------------------------------------------------

Continue for all characters

Final Frequency

e → 4
l → 2
o → 2
v → 1
t → 1
c → 1
d → 1

----------------------------------------------------------

Second Traversal

i = 0

Character = l

index = 11

freq[11] = 2

Skip

----------------------------------------------------------

i = 1

Character = o

index = 14

freq[14] = 2

Skip

----------------------------------------------------------

i = 2

Character = v

index = 21

freq[21] = 1

Return 2

Output

2

'''

# Frequency count(Hash Map)
class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

    
        for i in range(len(s)):  # finding first unique char 
            if freq[s[i]] == 1:
                return i

        return -1
    
s = "leetcode"
obj = Solution() 
print(obj.firstUniqChar(s))

# Frequency Count(Array)

class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = [0] * 26

        # Count frequency
        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] += 1

        # Find first unique character
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if freq[index] == 1:
                return i

        return -1
         
s = "loveleetcode"
obj = Solution()
print(obj.firstUniqChar(s))










