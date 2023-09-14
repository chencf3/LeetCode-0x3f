'''
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。

示例 1:
输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

示例 2:
输入: nums = [4,2,3,4]
输出: 4

提示:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
'''


### 方法一：暴力模拟，超时
# 时间复杂度：O(n ^ 3)
# 空间复杂度：O(1)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] > nums[k]:
                        res += 1
        return res


### 方法二：固定最长边，用相向双指针计算满足条件的情况
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(1)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res