class Solution:
    def intToRoman(self, num: int) -> str:
        rlt = ''
        qian = num // 1000
        rlt += 'M' * qian
        num -= qian * 1000

        bai = num // 100
        if bai < 4:
            rlt += 'C' * bai
        elif bai == 4:
            rlt += 'CD'
        elif bai < 9:
            rlt += 'D' + 'C' * (bai - 5)
        else:
            rlt += 'CM'
        num -= bai * 100

        shi = num // 10
        if shi < 4:
            rlt += 'X' * shi
        elif shi == 4:
            rlt += 'XL'
        elif shi < 9:
            rlt += 'L' + 'X' * (shi - 5)
        else:
            rlt += 'XC'
        num -= shi * 10

        ge = num
        if ge < 4:
            rlt += 'I' * ge
        elif ge == 4:
            rlt += 'IV'
        elif ge < 9:
            rlt += 'V' + 'I' * (ge - 5)
        else:
            rlt += 'IX'

        return rlt


if __name__ == "__main__":
    num = 1994
    sol = Solution()
    print(sol.intToRoman(num))
