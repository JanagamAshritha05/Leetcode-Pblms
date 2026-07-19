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

        

