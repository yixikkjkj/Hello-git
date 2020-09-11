class Solution:
    def threeSum1(self, nums):
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

    def threeSum2(self, nums):
        rlt = []
        if len(nums) < 3:
            return rlt
        nums.sort()
        i, j = 0, 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] and i < len(nums) - 2:
                i += 1
                j = i
                continue
            while j < len(nums) - 1:
                for k in range(len(nums) - 1, j, -1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        rlt.append([nums[i], nums[j], nums[k]])
                    elif nums[i] + nums[j] + nums[k] < 0:
                        break
                j += 1
            i += 1
            j = i + 1
        return rlt

    def threeSum(self, nums):
        rlt = []
        if len(nums) < 3:
            return rlt
        nums.sort()
        l, r = 0, 0
        for idx, num in enumerate(nums):
            if num > 0:
                return rlt
            if idx > 0 and num == nums[idx - 1]:
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + num == 0:
                    rlt.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                else:
                    r -= 1
        return rlt


if __name__ == "__main__":
    nums = [0,0,0]
    sol = Solution()
    print(sol.threeSum(nums))
