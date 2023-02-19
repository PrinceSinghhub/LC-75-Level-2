import collections


class Solution:
    def findOrder(self,n, prerequisites):
        src, dst = collections.Counter(), [set() for _ in range(n)]
        for d, s in prerequisites:
            src[d] += 1
            dst[s].add(d)
        ans = [x for x in range(n) if not src[x]]
        for s in ans:
            for d in dst[s]:
                src[d] -= 1
                if not src[d]:
                    ans.append(d)
        return ans if len(ans) == n else []
