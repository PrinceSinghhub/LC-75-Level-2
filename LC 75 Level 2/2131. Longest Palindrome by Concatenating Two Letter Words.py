class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        set_words = dict()
        count = 0
        flag = True

        for word in words:

            # If reverse exists add in pair (4)
            if word[::-1] in set_words and set_words[word[::-1]] > 0:
                count += 4
                set_words[word[::-1]] -= 1
            else:
                if word not in set_words:
                    set_words[word] = 1
                else:
                    set_words[word] += 1

        for word, value in set_words.items():
            # In the middle of the string we can add only one element with value are equal like: "aa", "bb"
            if flag and value == 1 and word[0] == word[1]:
                count += 2
                flag = False

        return count
