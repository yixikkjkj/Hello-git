class Solution:
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

        match_list = compilep()
        if not match_list:
            return False
        idx = 0
        for c in s:
            if idx >= len(match_list):
                return False
            while True:
                if idx >= len(match_list):
                    return False
                match = match_list[idx]
                if c != match[0] and match[0] != '.':
                    idx += 1
                else:
                    break
            if not match_list[idx].endswith('*'):
                idx += 1
        if idx < len(match_list):
            if not match_list[idx].endswith('*'):
                return False
            elif idx < len(match_list) - 1:
                return False
        return True


if __name__ == "__main__":
    s = "aaa"
    p = "a*a"
    sol = Solution()
    print(sol.isMatch(s, p))
