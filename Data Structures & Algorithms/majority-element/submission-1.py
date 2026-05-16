class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        max_count = 0
        majority = None
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1


        for k, v in hashMap.items():

            if v > max_count:
                max_count = v
                majority = k
        return majority




