class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height) - 1
        water = 0
        leftmax, rightmax = 0,0
        while left < right:
            leftmax = max(leftmax,height[left])
            rightmax = max(rightmax,height[right])
            if leftmax < rightmax:
                water += leftmax - height[left]
                left += 1
            else:
                water += rightmax - height[right]
                right -= 1
        return water