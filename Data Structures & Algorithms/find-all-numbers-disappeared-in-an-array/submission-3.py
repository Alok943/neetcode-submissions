class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for num in nums:
            value = abs(num) - 1
            nums[value] = -abs(nums[value])
        for i in range(0,n):
            if nums[i] > 0:
                result.append(i + 1)
        return result