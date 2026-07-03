class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        l, r = 0, n - 1
        while l <= r:
            ans[l] = nums[l]
            ans[l + n] = nums[l]
            
            ans[r] = nums[r]
            ans[r + n] = nums[r]
            l+=1
            r-=1

        return ans
        

        