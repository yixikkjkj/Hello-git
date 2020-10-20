class Solution:
    def fourSum(self, nums, target: int):
        if len(nums) < 4:
            return []
        nums.sort()
        i, j, k, m = 0, 0, 0, 0
        rlt = []
        while i < len(nums) - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < len(nums) - 2:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[len(nums) - 1] + nums[len(nums) - 2] < target:
                    continue
                k = j + 1
                m = len(nums) - 1
                while k < m:
                    tmp = nums[i] + nums[j] + nums[k] + nums[m]
                    if tmp == target:
                        rlt.append([nums[i], nums[j], nums[k], nums[m]])
                        k += 1
                        while k < m and nums[k - 1] == nums[k]:
                            k += 1
                    elif tmp > target:
                        m -= 1
                    else:
                        k += 1
                j += 1
            i += 1
        return rlt


if __name__ == "__main__":
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    sol = Solution()
    print(sol.fourSum(nums, target))
    print([[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2],
           [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
