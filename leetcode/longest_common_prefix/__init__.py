class Solution:
    def longestCommonPrefix(self, strs) -> str:
        rlt = ''
        if not strs:
            return rlt
        min_idx = min([len(s) for s in strs])
        idx = 0
        while idx < min_idx:
            c = strs[0][idx]
            for s in strs:
                if s[idx] != c:
                    return rlt
            rlt += c
            idx += 1
        return rlt


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))
