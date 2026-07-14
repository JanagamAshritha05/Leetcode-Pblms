'''
Problem Explanation

You are given two strings:

jewels → Characters that are considered jewels.
stones → All the stones you have.

Your task is to count how many stones are jewels.

Each occurrence should be counted.

Return the total number of jewel stones.

Example
jewels = "aA"
stones = "aAAbbbb"

Jewels:

a
A

Stones:

a
A
A
b
b
b
b

Count:

a  → 1
A  → 2

Answer:

3

Hidden Edge Cases

1. No jewel present

jewels = "a"
stones = "bbbb"

Output = 0

2. Every stone is a jewel
jewels = "abc"
stones = "abcabc"

Output = 6

3. Duplicate stones
jewels = "a"
stones = "aaaaaa"

Output = 6

Count every occurrence.

4. Uppercase and Lowercase
jewels = "A"
stones = "aaaaA"

Output = 1

A and a are different characters.

5. Mixed Characters
jewels = "ab"
stones = "aaabbccd"

Output = 5

6. No matching characters
jewels = "xyz"
stones = "abc"

Output = 0

Algorithm

Count the frequency of all stones.
Initialize count = 0.
Traverse each character in the stone frequency.
If the character exists in jewels, add its frequency to count.
Return count.

Pseudocode

Create stones_freq

Count frequency of stones

count = 0

for each character in stones_freq

      if character in jewels

            count += stones_freq[character]

return count

Dry Run

Input
jewels = "ab"

stones = "aaabbccd"
Step 1

Build stone frequency

a → 3
b → 2
c → 2
d → 1
Step 2

Initialize

count = 0
Step 3

Check each character

a in jewels ✔

count = 0 + 3 = 3
b in jewels ✔

count = 3 + 2 = 5
c in jewels ✘

Ignore
d in jewels ✘

Ignore
Final Answer
5

'''

# Frequency Count (HashMap)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        

        stones_freq = {}
        for ch in stones:
            stones_freq[ch] = stones_freq.get(ch, 0) + 1

        count = 0 
        for ch in stones_freq:
            if ch in jewels:
                count += stones_freq[ch] 
            
        return count 
    
obj = Solution() 
print(obj.numJewelsInStones("aA", "AAabc"))


#HashSet

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewel_set = set(jewels)

        count = 0

        for ch in stones:
            if ch in jewel_set:
                count += 1

        return count


obj = Solution() 
print(obj.numJewelsInStones("aA", "AAabc"))



