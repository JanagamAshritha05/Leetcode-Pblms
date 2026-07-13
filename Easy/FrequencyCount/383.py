'''
# LeetCode 383 – Ransom Note

### Recognition Trick

If the problem says:

* Can be formed
* Enough characters
* Use each character only once
* Construct one string from another

➡️ Think **Frequency Count**.

---

# Problem Explanation

You are given two strings:

* `ransomNote` → the string you want to create.
* `magazine` → the string containing available characters.

Each character in `magazine` can be used **only once**.

Return:

* `True` → if you can construct `ransomNote`.
* `False` → otherwise.

---

# Example

ransomNote = "aa"
magazine = "aab"

Need

a → 2

Available

a → 2
b → 1

Enough characters.

Output

True

---

# Hidden Edge Cases

### 1. Character Missing

ransomNote = "a"
magazine = "b"

Output = False

---

### 2. Frequency Not Enough

ransomNote = "aaa"
magazine = "aa"

Output = False

---

### 3. Extra Characters

ransomNote = "cat"
magazine = "catxyz"

Output = True

Extra letters do not matter.


### 4. Exact Match

ransomNote = "hello"
magazine = "hello"

Output = True

---

### 5. Magazine Smaller

ransomNote = "apple"
magazine = "app"

Output = False

---

# Algorithm

1. Count the frequency of `ransomNote`.
2. Count the frequency of `magazine`.
3. Compare both frequencies.
4. If any required character is greater than the available frequency, return `False`.
5. Otherwise, return `True`.

---

# Short Python Pseudocode

Create ransom_freq

Create magazine_freq

Count ransomNote frequency

Count magazine frequency

for each character in ransom_freq

      if ransom_freq > magazine_freq

            return False

return True

---

# Dry Run

### Input

ransomNote = "aa"

magazine = "aab"

---

### Step 1

ransom_freq

a → 2

---

### Step 2

magazine_freq

a → 2

b → 1

---

### Step 3

Compare

a

Need = 2

Available = 2

2 > 2 ❌

No problem found.

Return

True

---

### Another Dry Run

ransomNote = "aa"

magazine = "ab"

Need

a → 2

Available

a → 1

Compare

2 > 1 ✔

Return

False

---

# Time Complexity

O(n + m)

* `n` = length of `ransomNote`
* `m` = length of `magazine`

---

# Space Complexity

Dictionary Version

O(1)

Frequency Array Version

O(1)

(Because there are only 26 lowercase English letters.)

---

# Interview Trick

Whenever you see:

* Can be formed
* Enough characters
* Character can be used only once
* Construct one string from another

Think:

**Frequency Count → Compare Frequencies → Return True/False**

'''

# Frequency Count(Hash Map)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = {}
        for ch in ransomNote:
            ransom_freq[ch] = ransom_freq.get(ch, 0) + 1
            
        magazine_freq = {}
        for ch in magazine:
            magazine_freq[ch] = magazine_freq.get(ch, 0) + 1
        
        valid = True 
        for ch in ransom_freq:
            if ransom_freq[ch] > magazine_freq.get(ch, 0):
                valid = False 
                break 
        
        return valid
            
        
obj = Solution()
ransomNote = "a"
magazine = "b"
print(obj.canConstruct(ransomNote, magazine))


# Frequency Count (Array)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = [0]*26
        for ch in ransomNote:
            index = ord(ch) - ord('a')
            ransom_freq[index] += 1 
            
        magazine_freq = [0]*26
        for ch in magazine:
            index = ord(ch) - ord('a')
            magazine_freq[index] += 1
        
        valid = True 
        for i in range(26):
            if ransom_freq[i] > magazine_freq[i]:
                valid = False 
                break 
        
        return valid 
        
        
obj = Solution()
ransomNote = "a"
magazine = "b"
print(obj.canConstruct(ransomNote, magazine))












