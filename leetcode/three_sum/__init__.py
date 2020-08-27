class Solution:
    def threeSum(self, nums):
        rlt = []
        if len(nums) < 3:
            return rlt
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        a = [nums[i], nums[j], nums[k]]
                        a.sort()
                        if a not in rlt:
                            rlt.append(a)
        return rlt


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    print(sol.threeSum(nums))
