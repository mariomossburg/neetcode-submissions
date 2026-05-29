class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for i,v in enumerate(nums):
            hashMap[v] = hashMap.get(v, 0) + 1

        for i in hashMap.values():
            if i > 1:
                return True
        return False

        