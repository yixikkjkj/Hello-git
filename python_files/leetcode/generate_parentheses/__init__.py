class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pairs = 0
        while pairs< n:
            pairs += 1
