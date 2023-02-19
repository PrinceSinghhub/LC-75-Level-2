import collections
from collections import deque


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # use a dictionary to cache row and column
        n = len(stones)
        x = collections.defaultdict(list)
        y = collections.defaultdict(list)
        for stone in stones:
            i, j = tuple(stone)
            x[i].append(j)
            y[j].append(i)

        island = 0
        visited = set()
        while stones:  # count how many strong-connected components
            i, j = stones.pop()
            if (i, j) in visited:
                continue
            island += 1
            q = deque([(i, j)])
            while q:  # BFS
                for _ in range(len(q)):
                    a, b = q.popleft()
                    while x[a]:
                        ny = x[a].pop()
                        if (a, ny) in visited:
                            continue
                        visited.add((a, ny))
                        q.append((a, ny))
                    while y[b]:
                        nx = y[b].pop()
                        if (nx, b) in visited:
                            continue
                        visited.add((nx, b))
                        q.append((nx, b))

        return n - island