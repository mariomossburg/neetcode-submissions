class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        def dfs(i):
            if i == n:
                return
            
            ans[i] = nums[i]
            ans[i + n] = nums[i]

            dfs(i + 1)

        dfs(0)
        return ans
        