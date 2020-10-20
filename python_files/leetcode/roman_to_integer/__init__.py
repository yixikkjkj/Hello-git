class Solution:
    def romanToInt(self, s: str) -> int:
        c2val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        i = 0
        rlt = 0
        while i < len(s):
            val = c2val[s[i]]
            if i < len(s) - 1:
                next_val = c2val[s[i + 1]]
                if val < next_val:
                    i += 1
                    val = next_val - val
            rlt += val
            i += 1
        return rlt


if __name__ == "__main__":
    s = 'MCMXCIV'
    sol = Solution()
    print(sol.romanToInt(s))
