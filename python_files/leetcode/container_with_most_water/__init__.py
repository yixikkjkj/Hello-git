class Solution:
    # def maxArea(self, height) -> int:
    #     max_rlt = 0
    #     for i in range(len(height)):
    #         for j in range(i + 1, len(height)):
    #             curr_rlt = (j - i) * min(height[j], height[i])
    #             if curr_rlt > max_rlt:
    #                 max_rlt = curr_rlt
    #     return max_rlt

    def maxArea(self, height) -> int:
        i, j = 0, len(height) - 1
        max_rlt = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] < height[j]:
                old_i = i
                i += 1
                while i < j and height[old_i] > height[i]:
                    i += 1
            else:
                old_j = j
                j -= 1
                while i < j and height[j] < height[old_j]:
                    j -= 1
            curr_rlt = (j - i) * min(height[i], height[j])
            if curr_rlt > max_rlt:
                max_rlt = curr_rlt
        return max_rlt


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    sol = Solution()
    print(sol.maxArea(height))
