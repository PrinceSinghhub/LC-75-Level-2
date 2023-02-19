from collections import deque


class Solution(object):
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        pacific = deque([[0, j] for j in range(n)] + [[i, 0] for i in range(m)])
        atlantic = deque([[i, n - 1] for i in range(m)] + [[m - 1, i] for i in range(n)])

        def bfs(queue):
            visited = set()
            while queue:
                x, y = queue.popleft()
                visited.add((x, y))
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        if (x + dx, y + dy) not in visited:
                            if heights[x + dx][y + dy] >= heights[x][y]:
                                queue.append((x + dx, y + dy))
            return visited

        p, a = bfs(pacific), bfs(atlantic)

        return p.intersection(a)
