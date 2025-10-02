#Problem: Trapping Rain Water

#Problem Statement:
#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#Example
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: 6 units of water can be trapped.


def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    leftMax, rightMax = height[left], height[right]
    water = 0

    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, height[left])
            water += max(0, leftMax - height[left])
        else:
            right -= 1
            rightMax = max(rightMax, height[right])
            water += max(0, rightMax - height[right])
    
    return water

# Example usage
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Trapped Rain Water:", trap(height))
