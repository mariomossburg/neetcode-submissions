class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1 

        for i in hashMap.values():
            if i > 1:
                return True

        return False

        