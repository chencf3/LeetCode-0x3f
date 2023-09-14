'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：（图片见LeetCode）上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
'''


### 方法一：前后缀分解
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        pre_max, suf_max = [height[0]], [height[-1]]
        for i in range(1, n):
            pre_max.append(max(pre_max[-1], height[i]))
        for j in range(n - 2, -1, -1):
            suf_max.insert(0, max(suf_max[0], height[j]))
        for k in range(n):
            res += min(pre_max[k], suf_max[k]) - height[k]
        return res
        

### 方法二：相向双指针
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        left, right = 0, n - 1
        pre_max, suf_max = 0, 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max <= suf_max:
                res += pre_max - height[left]
                left += 1
            else:
                res += suf_max - height[right]
                right -= 1
        return res