from collections import deque


class Solution:
    def orangesRotting(self, grid):
        """
        queue = ((0,0))
        [2,2,0]
        [2,1,0]
        [0,1,1]

        """
        # put all the rotten orange into our tast queue.
        l = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, l))
                    grid[i][j] = 0

        while queue:
            I, J, l = queue.popleft()
            print(I, J)
            for i, j in [I - 1, J], [I + 1, J], [I, J - 1], [I, J + 1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    queue.append((i, j, l + 1))
                    grid[i][j] = 0
        # print(grid)
        if any(1 in row for row in grid):
            return -1
        else:
            return l