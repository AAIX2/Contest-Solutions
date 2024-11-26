class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # We will select the values based on their impact which is how big an interval can be because the higher the impact, it will cover more elements which we make sure we use less intervals
        # We sort the queries based on the first value
        queries.sort()
        # What we are trying to achieve is selecting some intervals which will be the candidates for our current ind since we have sorted the queries
        candidates = [] #Candidates will be a max heap since we want the maxright for current ind to get the maximum impact for every ind. Also we will be keeping only the rightmost ele of every query


        #  But we have filter out some of the candidates since we only need nums[i] candidates to make it 0 also we have to remove some elements from chosen as well since there could be a case where our minimum ind inside our chosen is lesser than cur ind which means it can never cover the cur ind, so we have to remove this ind from chosen as well and because of this we will need a min heap
        chosen = []
        j = 0
        ans = 0
        for i in range(n):
            while j<len(queries) and queries[j][0] == i:
                heapq.heappush(candidates,-queries[j][1])
                j+=1
            # Removing the current available indices 
            nums[i]-=len(chosen)
            
            while nums[i]>0 and candidates and abs(candidates[0])>=i:
                ans+=1
                c = -heapq.heappop(candidates)
                heapq.heappush(chosen,c)
                nums[i]-=1
            
            
            # In case even after applying all the queries nums[i] is still >0           
            if nums[i]>0:
                return -1
            # Removing all the elements from chosen that are less than curr ind since they wont be needed again
            
            while chosen and chosen[0] == i:
                heapq.heappop(chosen)
            
        return len(queries)-ans
            

