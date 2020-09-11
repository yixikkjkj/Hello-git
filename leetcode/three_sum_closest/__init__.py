class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        rlt = []
        if len(nums) < 3:
            return rlt
        nums.sort()
