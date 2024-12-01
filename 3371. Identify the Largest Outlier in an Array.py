# Using Hashmap
# Since the question says there are n-2 special elements so the sum of the special elements along with the element that is the sum of these elements gives the sum as 2*sum. So we can say 2*sum+outlier since outlier is the last remaining element so 2*sum+outlier == totalsum and from this relation we can get our answer
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        mp = Counter(nums)
        outlier = -1001
        for i in range(n):
            possibleOutlier = nums[i]
            diff = s-possibleOutlier
            if diff%2 == 0:
                mp[nums[i]]-=1
                if mp[diff//2]>0:
                    outlier = max(outlier,nums[i])
                mp[nums[i]]+=1
           
        return outlier
# Time Complexity- O(N)
# Space Complexity- O(N)
