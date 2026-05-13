import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l, r):
            if l >= r:
                return

            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            quicksort(l, p - 1)
            quicksort(p + 1, r)

        quicksort(0, len(nums) - 1)
        return nums

            
            