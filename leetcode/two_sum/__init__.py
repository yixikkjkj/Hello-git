class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return i, j
                j += 1
            i += 1
        return - 1, -1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        container = {}
        while i < len(nums):
            left = target - nums[i]
            if left in container:
                return container[left], i
            container[nums[i]] = i
            i += 1
        return -1, -1
