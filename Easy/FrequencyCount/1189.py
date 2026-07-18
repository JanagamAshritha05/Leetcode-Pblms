class Solution: #(BruteForce)
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = list(text)
        answer = 0 

        while True: 
            for ch in "balloon":
                if ch in chars:
                    chars.remove(ch) 
                else:
                    return answer 
            
            answer += 1

# FrequencyCount(HashMap)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balloon"

        text_freq = {}
        balloon_freq = {}

        # Count frequency of "balloon"
        for ch in balloon:
            balloon_freq[ch] = balloon_freq.get(ch, 0) + 1

        # Count frequency of input text
        for ch in text:
            text_freq[ch] = text_freq.get(ch, 0) + 1

        answer = float("inf")

        # Find the bottleneck character
        for ch in balloon_freq:
            available = text_freq.get(ch, 0)      # Safe lookup
            required = balloon_freq[ch]

            supported = available // required
            answer = min(answer, supported)

        return answer


# Frequency Count(Array) 
class Solution:
    def maxNumberOfBalloons(self, text: str):

        balloon = "balloon"

        text_freq = [0] * 26
        balloon_freq = [0] * 26

        # Count frequency of "balloon"
        for ch in balloon:
            balloon_freq[ord(ch) - ord('a')] += 1

        # Count frequency of input text
        for ch in text:
            text_freq[ord(ch) - ord('a')] += 1

        answer = float("inf")

        # Check only unique required characters
        for ch in "balon":

            index = ord(ch) - ord('a')

            available = text_freq[index]
            required = balloon_freq[index]

            supported = available // required

            answer = min(answer, supported)

        return answer

#Less Code
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}

        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1

        return min(
            freq.get('b', 0),
            freq.get('a', 0),
            freq.get('l', 0) // 2,
            freq.get('o', 0) // 2,
            freq.get('n', 0)
        )



