class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        i = 1
        for num in numbers:
            need = target - num
            if need in seen:
                return [seen[need],i]
            else:
                seen[num] = i
                i += 1