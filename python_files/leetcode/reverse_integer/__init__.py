class Solution:
    def reverse(self, x: int) -> int:
        under_zero = False
        if x < 0:
            under_zero = True
            x = -x

        s = 0
        while x:
            c = x % 10
            s = s * 10 + c
            x = x // 10

        if under_zero:
            s = -s
        if s > 2 ** 31 - 1 or s < -2 ** 31:
            return 0
        return s


if __name__ == "__main__":
    x = -120
    sol = Solution()
    print(sol.reverse(x))
