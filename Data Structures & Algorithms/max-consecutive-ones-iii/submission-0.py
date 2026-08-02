class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        zeroes = 0
        maxzeroes = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans