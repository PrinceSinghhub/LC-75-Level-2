class Solution:
    def longestCommonPrefix(self, strs):

        find_Smallest_String = min(strs, key=len)

        if len(strs) == 0 or len(find_Smallest_String) == 0:
            return ""

        prefix = ""
        for i in range(len(find_Smallest_String)):
            for s in strs:
                if find_Smallest_String[i] != s[i]:
                    return prefix
            prefix = find_Smallest_String[:i + 1]
        return prefix