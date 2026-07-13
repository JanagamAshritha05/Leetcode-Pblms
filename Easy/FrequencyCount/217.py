# 217 - Duplicates 

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

Pattern: Frequency Count (Hash Map)

Algorithm:

Create an empty frequency dictionary.
Traverse the array one element at a time.
If the current number is already in the dictionary, increase its frequency.
Otherwise, store its frequency as 1.
If the frequency of any number becomes 2, return True.
If the loop finishes without finding any duplicate, return False.
Python Pseudo Code
freq = {}

for each number in nums

      if number in freq

            freq[number] += 1

      else

            freq[number] = 1

      if freq[number] >= 2

            return True

return False

Dry Run:

Input

nums = [1, 2, 3, 1]
Initial
freq = {}
Step 1
Read 1

freq = {1:1}

Frequency of 1 = 1

Continue
Step 2
Read 2

freq = {1:1, 2:1}

Frequency of 2 = 1

Continue
Step 3
Read 3

freq = {1:1, 2:1, 3:1}

Frequency of 3 = 1

Continue
Step 4
Read 1

freq = {1:2, 2:1, 3:1}

Frequency of 1 = 2

Return True

'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num , 0) + 1

            if freq[num] >= 2:
                return True 
            
        return False 
    
obj = Solution()
print(obj.containsDuplicate([1,1,2,3,4]))


#
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        freq = {}

        i = 0

        while i < len(nums):

            num = nums[i]

            freq[num] = freq.get(num, 0) + 1

            if freq[num] >= 2:
                return True

            i += 1

        return False
    
obj = Solution() 
print(obj.containsDuplicate([1, 2, 3, 4]))



