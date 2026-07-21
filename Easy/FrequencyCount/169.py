#BruteForce 
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        majority_limit = n // 2

        for candidate in nums:
            count = 0

            for num in nums:
                if candidate == num:
                    count += 1

            if count > majority_limit:
                return candidate

# FreqCount(HashMap)
class Solution:
    def majorityElement(self, nums):
        size = len(nums)
        majority_limit = size // 2

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            if freq[num] > majority_limit:
                return num

