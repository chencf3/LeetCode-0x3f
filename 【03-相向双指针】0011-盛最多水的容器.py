'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：（图片见LeetCode）图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

提示：
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
'''


### 方法一：暴力模拟，超时
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, (j - i) * min(height[i], height[j]))
        return res


### 方法二：相向双指针
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res