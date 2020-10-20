class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getJishuLongPalin(idx):
            target = c
            i = 1
            while idx - i >= 0 and idx + i < len(s):
                if s[idx - i] == s[idx + i]:
                    target = s[idx - i] + target + s[idx + i]
                else:
                    return target
                i += 1
            return target

        def getOushuLongPalin(idx):
            target = s[idx] + s[idx + 1]
            i = 1
            while idx - i >= 0 and idx + i + 1 < len(s):
                if s[idx - i] == s[idx + i + 1]:
                    target = s[idx - i] + target + s[idx + i + 1]
                else:
                    return target
                i += 1
            return target

        target_str = ''
        for idx, c in enumerate(s):
            jishu_str = getJishuLongPalin(idx)
            oushu_str = c
            if idx < len(s) - 1 and s[idx] == s[idx + 1]:
                oushu_str = getOushuLongPalin(idx)
            palin_str = jishu_str if len(jishu_str) > len(oushu_str) else oushu_str
            if len(palin_str) > len(target_str):
                target_str = palin_str

        return target_str



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans


if __name__ == "__main__":
    s = "cbb"
    sol = Solution()
    print(sol.longestPalindrome(s))
