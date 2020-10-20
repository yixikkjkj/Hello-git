class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        rlt = []
        if len(nums) < 3:
            return rlt
        nums.sort()

        i, j, k = 0, 0, 0
        best = 2**64
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                judge = nums[i] + nums[j] + nums[k]
                if judge == target:
                    return target
                if abs(judge - target) < abs(best - target):
                    best = judge
                if judge > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif judge < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

            i += 1

        return best


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    print(sol.threeSumClosest(nums, target))
