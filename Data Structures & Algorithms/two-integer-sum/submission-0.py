class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        for num in nums:
            need = target - num
            if need in seen:
                return [seen[need],i]
            else:
                seen[num] = i
                i += 1