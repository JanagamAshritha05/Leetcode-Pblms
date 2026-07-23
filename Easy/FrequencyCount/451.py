class Solution: #(BruteForce)
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        sorted_chars = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        
        ans = []
        for ch, count in sorted_chars:
            for i in range(count):
                ans.append(ch) 
        
        return "".join(ans)

#(Hashmap + BucketSort)
class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Step 1: Count frequency of each character
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1


        # Step 2: Create bucket array
        bucket_arr = [[] for _ in range(len(s) + 1)]


        # Step 3: Put characters into their frequency bucket
        for ch, frequency in freq.items():
            bucket_arr[frequency].append(ch)


        # Step 4: Build answer from highest frequency to lowest
        ans = []

        for frequency in range(len(s), 0, -1):
            for ch in bucket_arr[frequency]:
                for _ in range(frequency):
                    ans.append(ch)


        # Step 5: Convert list to string
        return "".join(ans)

