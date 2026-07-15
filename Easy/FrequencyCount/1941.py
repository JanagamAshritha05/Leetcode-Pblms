class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        expected = s.count(s[0])

        for ch in s:
            if s.count(ch) != expected:
                return False

        return True

# 

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        expected = freq[ch]
        for ch in freq:
            if freq[ch] != expected:
                return False
        return True
    
# 
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        freq = [0] * 26

        # Count frequency
        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] += 1

        expected = 0

        # Find first non-zero frequency
        for count in freq:
            if count != 0:
                expected = count
                break

        # Compare all non-zero frequencies
        for count in freq:
            if count != 0 and count != expected:
                return False

        return True




