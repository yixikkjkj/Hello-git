class Solution:
    def letterCombinations(self, digits: str):
        digit2letterlist = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if len(digits) <= 0:
            return []
        rlt = [data for data in digit2letterlist[digits[0]]]
        for idx in range(1, len(digits)):
            tmps = []
            c = digits[idx]
            if c not in digit2letterlist:
                return ''
            letter_list = digit2letterlist[c]
            for letter in letter_list:
                for rlt_str in rlt:
                    rlt_str += letter
                    tmps.append(rlt_str)

            rlt = tmps
        return rlt


if __name__ == "__main__":
    digits = '234'
    sol = Solution()
    print(sol.letterCombinations(digits))
