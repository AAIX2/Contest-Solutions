# Using dp on trees
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges)+1
        adj = {node:[] for node in range(n)}
        for n1,n2,wt in edges:
            adj[n1].append([n2,wt])
            adj[n2].append([n1,wt])
        dp = [[-1 for i in range(2)]for i in range(n)]
        def dfs(node,par,isParentEdgeRemoved):
            if dp[node][isParentEdgeRemoved]!=-1:
                return dp[node][isParentEdgeRemoved]
            edgesToRemove = len(adj[node])-k-isParentEdgeRemoved
            ans = 0
            candidates = []
            for nei,wt in adj[node]:
                if nei!=par:
                    dontRemove = dfs(nei,node,0)+wt
                    remove = dfs(nei,node,1)
                    candidates.append([dontRemove,remove])
            candidates.sort(key = lambda x: x[0]-x[1])
            for i in range(len(candidates)):
                dontRemove = candidates[i][0]
                remove = candidates[i][1]
                if i<edgesToRemove:
                    ans+=remove
                else:
                    ans+=max(remove,dontRemove)
            dp[node][isParentEdgeRemoved] = ans
            return dp[node][isParentEdgeRemoved]
        return dfs(0,-1,0)