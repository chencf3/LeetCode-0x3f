'''
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 
提示：
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
'''

### 方法一：相向双指针
# 时间复杂度：O(n ^ 3)
# 空间复杂度：O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        i = 0
        while i < n - 3:
            x = nums[i]
            if x + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:
                while i < n - 3 and nums[i] == x:
                    i += 1
            j = i + 1
            while j < n - 2:
                y = nums[j]
                if x + y + nums[j + 1] + nums[j + 2] > target:
                    break
                if x + y + nums[-2] + nums[-1] < target:
                    while j < n - 2 and nums[j] == y:
                        j += 1
                left, right = j + 1, n - 1
                while left < right:
                    y, z, m = nums[j], nums[left], nums[right]
                    tot = x + y + z + m
                    if tot == target:
                        res.append([x, y, z, m])
                        while left < right and nums[right] == m:
                            right -= 1
                        while left < right and nums[left] == z:
                            left += 1
                    elif tot > target:
                        while left < right and nums[right] == m:
                            right -= 1
                    else:
                        while left < right and nums[left] == z:
                            left += 1
                while j < n - 2 and nums[j] == y:
                    j += 1
            while i < n - 3 and nums[i] == x:
                i += 1
        return res