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
            return float(self.getK(nums1, nums2, (total + 1) // 2 - 1))
        else:
            return (self.getK(nums1, nums2, total // 2 - 1) + self.getK(nums1, nums2, total // 2)) / 2

    def getK(self, nums1, nums2, k):
        temp_k = k
        idx1, idx2 = 0, 0
        while True:
            if idx1 == len(nums1):
                return nums2[idx2 + k]
            if idx2 == len(nums2):
                return nums1[idx1 + k]
            if k == 0:
                return min(nums1[idx1], nums2[idx2])

            validx1 = min(idx1 + (k - 1) // 2, len(nums1) - 1)
            validx2 = min(idx2 + (k - 1) // 2, len(nums2) - 1)
            if nums1[validx1] <= nums2[validx2]:
                k -= validx1 - idx1 + 1
                idx1 = validx1 + 1
            else:
                k -= validx2 - idx2 + 1
                idx2 = validx2 + 1


if __name__ == "__main__":
    nums1 = [1]
    nums2 = [3, 4]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
