# Using BFS

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n,m = len(edges1)+1,len(edges2)+1
        adj1 = {node:[] for node in range(n)}
        adj2 = {node:[] for node in range(m)}
        for n1,n2 in edges1:
            adj1[n1].append(n2)
            adj1[n2].append(n1)
        for n1,n2 in edges2:
            adj2[n1].append(n2)
            adj2[n2].append(n1)
        # print(adj1)
        def bfs(st,k,adj):
            cnt = 0
            q = deque([[st,-1]])
            dist = 0
            while q and dist<=k:
                for i in range(len(q)):
                    node,par = q.popleft()
                    cnt+=1
                    for nei in adj[node]:
                        if nei!=par:
                            q.append([nei,node])
                dist+=1
            return cnt
        ans = [0 for i in range(n)]
        for i in range(n):
            ans[i] = bfs(i,k,adj1)
             
        maxi = 0
        for i in range(m):
            maxi = max(maxi,bfs(i,k-1,adj2))
            
        for i in range(n):
            ans[i]+=maxi
        return ans
# Time Complexity- O(N**2+M**2)
# Space Complexity- O(N+M)


