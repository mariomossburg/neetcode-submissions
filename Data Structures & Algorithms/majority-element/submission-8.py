class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        max_count = 0
        candidate = None

        for n in nums:
            d[n] = d.get(n, 0) + 1


        for k, v in d.items():
            if v > max_count:
                max_count = v
                candidate = k
        return candidate
        