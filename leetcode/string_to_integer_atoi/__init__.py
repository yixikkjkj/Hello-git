class Solution:
    def myAtoi(self, integer_str: str) -> int:
        def rlt_guifan(val):
            if below_zero:
                val = -val
            if val < -2 ** 31:
                return - 2 ** 31
            if val > 2 ** 31 - 1:
                return 2 ** 31 - 1
            return val

        integer_str = integer_str.strip()
        if not integer_str:
            return 0
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        below_zero = False
        first = integer_str[0]
        if not first in nums:
            if first == '-':
                below_zero = True
            elif first != '+':
                return 0
            integer_str = integer_str[1:]
        rlt = 0
        for num in integer_str:
            if num not in nums:
                return rlt_guifan(rlt)
            rlt = rlt * 10 + nums.index(num)
        return rlt_guifan(rlt)


if __name__ == "__main__":
    string = "-91283472332"
    sol = Solution()
    print(sol.myAtoi(string))
