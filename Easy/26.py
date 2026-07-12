# Remove Duplicates from sorted array
'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the uniqu387e numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.


Pattern - two pointers

Algorithm:

1. Place the slow pointer at the first element.
2. Place the fast pointer at the second element.
3. Compare the elements at slow and fast.
4. If they are different:
      Move slow one step forward.
      Copy nums[fast] to nums[slow].
5. Move fast one step forward.
6. Repeat until fast reaches the end.
7. Return slow + 1.

Pseudo code:

slow = 0
fast = 1

while fast < length of nums:

      if nums[fast] != nums[slow]:

            slow++

            nums[slow] = nums[fast]

      fast++

return slow + 1

Dry Run:

Input:
nums = [0,0,1,1,1,2,2,3,3,4]

Initial:
slow = 0
fast = 1

Step 1:
nums[slow] = 0
nums[fast] = 0
Same → Move fast

slow = 0
fast = 2

--------------------------------

Step 2:
nums[slow] = 0
nums[fast] = 1
Different

Move slow
slow = 1

Copy
nums[1] = 1

Array:
[0,1,1,1,1,2,2,3,3,4]

fast = 3

--------------------------------

Step 3:
nums[slow] = 1
nums[fast] = 1
Same → Move fast

fast = 4

--------------------------------

Step 4:
nums[slow] = 1
nums[fast] = 1
Same → Move fast

fast = 5

--------------------------------

Step 5:
nums[slow] = 1
nums[fast] = 2
Different

Move slow
slow = 2

Copy
nums[2] = 2

Array:
[0,1,2,1,1,2,2,3,3,4]

fast = 6

--------------------------------

Step 6:
nums[slow] = 2
nums[fast] = 2
Same → Move fast

fast = 7

--------------------------------

Step 7:
nums[slow] = 2
nums[fast] = 3
Different

Move slow
slow = 3

Copy
nums[3] = 3

Array:
[0,1,2,3,1,2,2,3,3,4]

fast = 8

--------------------------------

Step 8:
nums[slow] = 3
nums[fast] = 3
Same → Move fast

fast = 9

--------------------------------

Step 9:
nums[slow] = 3
nums[fast] = 4
Different

Move slow
slow = 4

Copy
nums[4] = 4

Final Array:
[0,1,2,3,4,2,2,3,3,4]

Return:
k = slow + 1 = 5

Unique Elements:
[0,1,2,3,4]


'''
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        slow = 0
        fast = 1

        while fast < len(nums):

            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

            fast += 1

        return slow + 1


nums = [0,0,1,1,1,2,2,3,3,4]

obj = Solution()

k = obj.removeDuplicates(nums)

print("k =", k)
print("Unique Elements =", nums[:k])


