# Find words that can be formed by characters 
'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.


Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


## Pattern

**Frequency Count (HashMap / Dictionary)**

**Recognition Trick**

If the problem asks:

* Count characters
* Check if a word can be formed
* Compare two strings
* Enough occurrences of each character

➡️ Think **Frequency Count**.

---

# Hidden Edge Cases

### Edge Case 1

words = ["cat"]
chars = "tac"

Output = 3

Reason:

All required characters are available.

---

### Edge Case 2

words = ["cat"]
chars = "ta"

Output = 0

Reason:

Character 'c' is missing.

---

### Edge Case 3

words = ["book"]
chars = "bok"

Output = 0

Reason:

Need

o → 2

Available

o → 1

Character exists, but frequency is not enough.

---

### Edge Case 4

words = ["hello"]
chars = "helo"

Output = 0

Reason:

Need

l → 2

Available

l → 1

---

### Edge Case 5

words = ["cat"]
chars = "catxyz"

Output = 3

Reason:

Extra characters do not matter.

---

### Edge Case 6

words = ["a","bb","ccc"]
chars = "abccc"

Output = 4

Reason:

"a"  ✔

"bb" ✘

"ccc" ✔

Answer = 1 + 3 = 4

---

# Algorithm

1. Create a frequency dictionary for `chars`.
2. Initialize `count = 0`.
3. Traverse each word in `words`.
4. Create a frequency dictionary for the current word.
5. Compare the word frequency with the `chars` frequency.
6. If every character of the word is available with enough frequency, add the length of the word to `count`.
7. Return `count`.

---

# Python Pseudo Code

Create freq of chars

count = 0

for each word

      Create freq of word

      Compare word_freq with chars_freq

      If valid

            count += length of word

return count

---

# Dry Run

### Input

words = ["cat","bt","hat","tree"]

chars = "atach"


### Step 1

Build frequency of chars

freq =

{
a : 2
t : 1
c : 1
h : 1
}


---

### Word = "cat"

word_freq =

{
c : 1
a : 1
t : 1
}


Compare

c : 1 <= 1 ✔

a : 1 <= 2 ✔

t : 1 <= 1 ✔

Valid


count = 3

---

### Word = "bt"


word_freq =

{
b : 1
t : 1
}


Compare

b : 1 <= 0 ✘

Invalid

count = 3

---

### Word = "hat"

word_freq =

{
h : 1
a : 1
t : 1
}

Compare

h : 1 <= 1 ✔

a : 1 <= 2 ✔

t : 1 <= 1 ✔

Valid

count = 6

---

### Word = "tree"

word_freq =

{
t : 1
r : 1
e : 2
}

Compare

t : 1 <= 1 ✔

r : 1 <= 0 ✘

Invalid

Final

count = 6

Output
6

# Interview Trick

Whenever you see:

* Can be formed
* Enough characters
* Character frequency
* Compare two strings

Think:

**Build Frequency → Compare Frequency → Add Answer**


'''
#Frequency Count (Hash Map)

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:

        # Frequency of chars
        freq = {}

        for ch in chars:
            freq[ch] = freq.get(ch, 0) + 1

        count = 0

        # Check each word
        for word in words:

            # Frequency of current word
            word_freq = {}

            for ch in word:
                word_freq[ch] = word_freq.get(ch, 0) + 1

            valid = True

            # Compare frequencies
            for ch in word_freq:

                if word_freq[ch] > freq.get(ch, 0):
                    valid = False
                    break

            if valid:
                count += len(word)

        return count


words = ["cat","bt","hat","tree"]
chars = "atach"
obj = Solution() 
print(obj.countCharacters(words, chars))
