class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        longest = 0
        for c in s:
            if c in sub:
                sub = sub[sub.index(c) + 1:]
            sub.append(c)
            if len(sub) > longest:
                longest = len(sub)

        return longest


if __name__ == "__main__":
    s = 'abcabcbb'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
