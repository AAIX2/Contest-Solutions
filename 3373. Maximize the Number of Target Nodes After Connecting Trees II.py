# Using concept of dp on trees

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1)+1
        m = len(edges2)+1
        adj1 = {node:[] for node in range(n)}
        adj2 = {node:[] for node in range(m)}
        for n1,n2 in edges1:
            adj1[n1].append(n2)
            adj1[n2].append(n1)
        for n1,n2 in edges2:
            adj2[n1].append(n2)
            adj2[n2].append(n1)
        # Getting the even and odd count of the node and its subtree
        evenSubTree1 = [0]*n
        oddSubTree1 = [0]*n
        def dfs1Tree1(node,par):
            evenSubTree1[node] = 1
            oddSubTree1[node] = 0
            for i in adj1[node]:
                if i!=par:
                    dfs1Tree1(i,node)
                    evenSubTree1[node]+=oddSubTree1[i]
                    oddSubTree1[node]+=evenSubTree1[i]
        # Getting the total even and odd count of nodes at even dist for all the nodes
        totalEven1Node = [0]*n
        totalOdd1Node = [0]*n
        def dfs2Tree1(node,par,evenAbove,oddAbove):
            totalEven1Node[node]+=evenSubTree1[node]+evenAbove
            totalOdd1Node[node]+=oddSubTree1[node]+oddAbove

            for i in adj1[node]:
                if i!=par:
                    evenUp = totalOdd1Node[node]-evenSubTree1[i]
                    oddUp = totalEven1Node[node]-oddSubTree1[i]
                    dfs2Tree1(i,node,evenUp,oddUp)
        # Same stuff for tree 2
        evenSubTree2 = [0]*m
        oddSubTree2 = [0]*m
        def dfs1Tree2(node,par):
            evenSubTree2[node] = 1
            oddSubTree2[node] = 0
            for i in adj2[node]:
                if i!=par:
                    dfs1Tree2(i,node)
                    evenSubTree2[node]+=oddSubTree2[i]
                    oddSubTree2[node]+=evenSubTree2[i]


        totalEven2Node = [0]*m
        totalOdd2Node = [0]*m
        def dfs2Tree2(node,par,evenAbove,oddAbove):
            totalEven2Node[node]+=evenSubTree2[node]+evenAbove
            totalOdd2Node[node]+=oddSubTree2[node]+oddAbove

            for i in adj2[node]:
                if i!=par:
                    evenUp = totalOdd2Node[node]-evenSubTree2[i]
                    oddUp = totalEven2Node[node]-oddSubTree2[i]
                    dfs2Tree2(i,node,evenUp,oddUp)
        dfs1Tree1(0,-1)
        dfs2Tree1(0,-1,0,0)
        dfs1Tree2(0,-1)
        dfs2Tree2(0,-1,0,0)
        # Since we connect the edge to the node with maximum neighbors that are at an odd distance. Odd distance because we are connecting one node of tree1 to another node of tree2 so because of that edge all the distances from the nodes in tree2 will become odd.  
        maxOdd = max(totalOdd2Node)
        ans = [0]*n
        for i in range(n):
            ans[i] = totalEven1Node[i]+maxOdd
        return ans
# Time Complexity- O(N+M)
# Space Complexity- O(N+M)