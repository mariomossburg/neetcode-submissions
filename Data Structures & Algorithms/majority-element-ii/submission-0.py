class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        for i, v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1

        for i in dic.items():
            if i[1] > len(nums) / 3:
                res.append(i[0])
        return res

        