'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

Easy Algorithm to Remember

Start from the last digit of both strings.
Add the current digits and the carry.
Store the last digit of the sum (% 10).
Store the carry (// 10).
Move one step left in both strings.
Repeat until both strings are finished and there is no carry left.
Return the answer.

Important Constraint (Most Important)

❌ You cannot do this:

int(num1)
int(num2)

or

eval()

or use any BigInteger libraries.

The interviewer wants you to perform addition manually, just like adding numbers on paper

'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        ans = ""

        while i >= 0 or j >= 0 or carry: #If carry is not 0, keep the loop running one more time

            total = carry

            if i >= 0:
                total += int(num1[i])
                i -= 1

            if j >= 0:
                total += int(num2[j])
                j -= 1

            ans = str(total % 10) + ans
            carry = total // 10

        return ans

obj = Solution() 
print(obj.addStrings("999", "1"))

#
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        ans = ""

        n = max(len(num1), len(num2))

        for k in range(n):

            total = carry

            if i >= 0:
                total += int(num1[i])
                i -= 1

            if j >= 0:
                total += int(num2[j])
                j -= 1

            ans = str(total % 10) + ans
            carry = total // 10

        if carry:
            ans = str(carry) + ans

        return ans


obj = Solution()
print(obj.addStrings("999", "1"))







