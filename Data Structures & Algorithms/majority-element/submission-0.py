class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(0,n):
            if count == 0:
                candidate = nums[i]
                count +=1
            elif candidate == nums[i]:
                count+=1
            else:
                count -= 1
        return candidate