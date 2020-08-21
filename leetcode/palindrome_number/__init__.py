class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_list = []
        while x > 0:
            num_list.append(x % 10)
            x = x // 10
        for i in range(len(num_list) // 2):
            if num_list[i] != num_list[len(num_list) - 1 - i]:
                return False
        return True


if __name__ == "__main__":
    num = 1231
    sol = Solution()
    print(sol.isPalindrome(num))
