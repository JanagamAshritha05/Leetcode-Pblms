class Solution:
    def commonChars(self, words):
        answer = []
        processed = set()

        first_word = words[0]

        for ch in first_word:

            if ch in processed:
                continue

            processed.add(ch)

            minimum_count = float('inf')

            for word in words:
                current_count = word.count(ch)
                minimum_count = min(minimum_count, current_count)

            for _ in range(minimum_count):
                answer.append(ch)

        return answer

        
# FreqCount (HashMap)

class Solution:
    def commonChars(self, words):
        
        answer = []

        # Frequency of first word
        common_freq = {}

        for ch in words[0]:
            common_freq[ch] = common_freq.get(ch, 0) + 1


        # Compare with remaining words
        for word in words[1:]:

            current_freq = {}

            # Count current word frequency
            for ch in word:
                current_freq[ch] = current_freq.get(ch, 0) + 1


            # Keep minimum frequency
            for ch in common_freq:
                common_freq[ch] = min(
                    common_freq[ch],
                    current_freq.get(ch, 0)
                )


        # Build answer
        for ch, count in common_freq.items():
            for _ in range(count):
                answer.append(ch)


        return answer

#FreqCount(Array)

class Solution:
    def commonChars(self, words):

        answer = []

        # Frequency of first word
        common_freq = [0] * 26

        for ch in words[0]:
            index = ord(ch) - ord('a')
            common_freq[index] += 1


        # Compare with remaining words
        for word in words[1:]:

            current_freq = [0] * 26

            # Count current word
            for ch in word:
                index = ord(ch) - ord('a')
                current_freq[index] += 1


            # Keep minimum frequency
            for i in range(26):
                common_freq[i] = min(
                    common_freq[i],
                    current_freq[i]
                )


        # Build answer
        for i in range(26):

            while common_freq[i] > 0:
                answer.append(chr(i + ord('a')))
                common_freq[i] -= 1


        return answer


