
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        que = deque()
        fresh = 0
        opr = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1

                if grid[i][j] == 2:
                    que.append((i,j))

        while que:
            opr += 1
            for _ in range(len(que)):
                
                i,j = que.popleft()
                
                # top
                if  i > 0 and grid[i-1][j] == 1:
                    fresh -= 1
                    grid[i-1][j] = 2
                    que.append((i-1,j))
                
                # bottom
                if i < n-1 and grid[i+1][j] == 1:
                    print(9999)
                    fresh -= 1
                    grid[i+1][j] = 2
                    que.append((i+1,j))
                # left
                if j > 0 and grid[i][j-1] == 1:
                    fresh -= 1
                    grid[i][j-1] = 2
                    que.append((i,j-1))
                # right
                if j < m-1 and grid[i][j+1] == 1:
                    fresh -= 1
                    grid[i][j+1] = 2
                    que.append((i,j+1))
       
        return -1 if fresh > 0 else max(0,opr-1)
