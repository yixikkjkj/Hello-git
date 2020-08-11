class Solution1:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i, j = 0, 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            nums.extend(nums1[i:])
        if j < len(nums2):
            nums.extend(nums2[j:])
        if len(nums) % 2:
            return float(nums[int((len(nums) - 1) / 2)])
        else:
            idx = int(len(nums) / 2) - 1
            return (nums[idx] + nums[idx + 1]) / 2


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total = len(nums1) + len(nums2)
        if total % 2:
            idx = int((total - 1) / 2)
        else:
            idx = total / 2 - 1

        # 在两个正序列表中找到 idx 位置的数
        f1, f2 = 0, 0
        i, j = idx / 2 - 1, idx / 2 - 1
        while i + j != idx:
            pass


if __name__ == "__main__":
    nums1 = [1]
    nums2 = [3, 4]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
