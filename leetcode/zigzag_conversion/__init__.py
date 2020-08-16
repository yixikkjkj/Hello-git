class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        signal_total = 2 * numRows - 2  # numRows > 1
        rlt = ''
        i = 0
        while i < len(s):
            rlt += s[i]
            i += signal_total
        for i in range(1, numRows - 1):
            idx = i
            while idx < len(s):
                rlt += s[idx]
                if idx + signal_total - i * 2 < len(s):
                    rlt += s[idx + signal_total - i * 2]
                idx += signal_total

        i = 0
        while i + numRows - 1 < len(s):
            rlt += s[i + numRows - 1]
            i += signal_total

        return rlt


"""
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

"""
P   A   H   N
A P L S I I G
Y   I   R
"""

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numsRow = 3
    sol = Solution()
    print(sol.convert(s, numsRow))
