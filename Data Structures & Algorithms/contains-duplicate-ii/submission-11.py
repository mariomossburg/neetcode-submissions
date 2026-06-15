class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # does the algorithm contain 2 values 
        # were are at most k distance apart?
        
        l = len(nums) - 1

        for i in range(l):
            r = i + 1
            while r <= l:
                if nums[i] == nums[r] and r-i <= k:
                    return True
                r+=1
        return False
            

