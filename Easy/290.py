'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
a → dog
b → cat
b → cat
a → fish ❌
One character cannot maps to two different words

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
a → dog
a → cat ❌
The same character cannot map to different words.

Output: false 

Example 4:
pattern = "abba"
s = "dog dog dog dog"

a → dog
b → dog ❌
Two different characters cannot map to the same word

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

'''
# Brute Force Method 
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False 

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in char_to_word:
                if char_to_word[char] != word:
                    return False 
            else:
                char_to_word[char] = word 

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False 
            else:
                word_to_char[word] = char 

        return True 

obj = Solution()
print(obj.wordPattern("abba", "dog cat cat dog"))


#
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False 

        char_to_word = {}
        used_words = set()

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in char_to_word:
                if char_to_word[char] != word:
                    return False 
            else:
                if word in used_words:
                    return False 
                char_to_word[char] = word 
                used_words.add(word)

        return True 


obj = Solution() 
print(obj.wordPattern("aaaa", "dog cat cat dog"))






