class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, value in enumerate(nums); 
            r = target - value
            if r in d: return [index, d[r]]
            d[j] = index 
