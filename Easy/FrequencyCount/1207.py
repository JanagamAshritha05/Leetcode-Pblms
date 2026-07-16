class Solution: #(BruteForce)
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):

                if arr[i] != arr[j]: # Compare only different numbers

                    freq1 = arr.count(arr[i])   # Find their frequencies
                    freq2 = arr.count(arr[j])

                    if freq1 == freq2: # If frequencies are same, answer is False
                        return False

        return True

#FrequencyCount(HashSet)
class Solution: 
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        # Count the frequency of each number
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        seen = set()

        # Check whether each frequency is unique
        for count in freq.values():
            if count in seen:
                return False
            seen.add(count)

        return True


