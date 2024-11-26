class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        # If you observe we can only reach (n-1,n-1) in n-1 moves so there is only one way in which the first child can move which is diagonally
        firstChild = 0
        for i in range(n):
            firstChild+=fruits[i][i]
        # Second child can move in 3 different direction but if u observe we can see that the child can reach (n-1,n-1) cell in n-1 steps if and only if it is less than equal to diagonal but we know the diagonal elements are already consumed by the first child so there is no point in going there so in this way we only have cells which are less than our diagonal. The same goes for third child as well.


        # Also in this way we made the 3 chidren independent of each other rather than doing them simultaneously which is a lot more complex.
        dirSecondChild_x = [1,1,1]
        dirSecondChild_y = [-1,0,1]
        dp = [[-1 for i in range(n)]for i in range(n)]
        def solveTopRight(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            ans = fruits[i][j]
            for d in range(3):
                new_x,new_y = i+dirSecondChild_x[d],j+dirSecondChild_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<n:
                    if new_x<new_y:
                        ans = max(ans,fruits[i][j]+solveTopRight(new_x,new_y))
            dp[i][j] = ans
            return dp[i][j]

        secondChild = solveTopRight(0,n-1)

        dirThirdChild_x = [-1,0,1]
        dirThirdChild_y = [1,1,1]
        dp1 = [[-1 for i in range(n)]for i in range(n)]
        def solveBottomLeft(i,j):
            if dp1[i][j]!=-1:
                return dp1[i][j]
            ans = fruits[i][j]
            for d in range(3):
                new_x,new_y = i+dirThirdChild_x[d],j+dirThirdChild_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<n:
                    if new_x>new_y:
                        ans = max(ans,fruits[i][j]+solveBottomLeft(new_x,new_y))
            dp1[i][j] = ans
            return dp1[i][j]
        thirdChild = solveBottomLeft(n-1,0)
        return firstChild+secondChild+thirdChild