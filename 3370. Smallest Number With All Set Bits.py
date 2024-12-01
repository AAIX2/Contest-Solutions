# Using Bit manipulation

class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        for i in range(10):
            if n&(1<<i) == 1:
                ans|=(1<<i)
            else:
                ans|=(1<<i)
            if ans>=n:
                return ans
# Time Complexity- O(1)
# Space Complexity- O(1)