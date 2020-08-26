class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        def compilep():
            compiled_list = []
            for c in p:
                if c == '*':
                    if not compiled_list:
                        return None
                    if compiled_list[-1].endswith('*'):
                        return None
                    compiled_list[-1] += c
                else:
                    compiled_list.append(c)
            return compiled_list

        def is_match(sig, mat):
            if len(mat) == 1:
                return sig == mat or mat == '.'
            return sig == mat[0] or mat[0] == '.'

        match_list = compilep()
        if not match_list:
            return False
        idx = len(match_list) - 1
        for i in range(len(s) - 1, -1, -1):
            if idx < 0:
                return False
            while True:
                if idx < 0:
                    return False
                if is_match(s[i], match_list[idx]):
                    if len(match_list[idx]) == 1:
                        idx -= 1
                    break
                if len(match_list[idx]) == 2:
                    idx -= 1
                else:
                    return False
        if idx >= 0:
            for j in range(0, idx + 1):
                if len(match_list[j]) == 1:
                    return False
        return True

        # idx = 0
        # for c in s:
        #     if idx >= len(match_list):
        #         return False
        #     while True:
        #         if idx >= len(match_list):
        #             return False
        #         match = match_list[idx]
        #         if c != match[0] and match[0] != '.':
        #             idx += 1
        #         else:
        #             break
        #     if not match_list[idx].endswith('*'):
        #         idx += 1
        # if idx < len(match_list):
        #     if not match_list[idx].endswith('*'):
        #         return False
        #     elif idx < len(match_list) - 1:
        #         return False
        # return True


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


if __name__ == "__main__":
    s = "aaaaaa"
    p = "ab*a*c*a"
    sol = Solution()
    print(sol.isMatch(s, p))
