'''
我们定义 arr 是 山形数组 当且仅当它满足：
arr.length >= 3
存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给你整数数组 nums​ ，请你返回将 nums 变成 山形状数组 的​ 最少 删除次数。

示例 1：
输入：nums = [1,3,1]
输出：0
解释：数组本身就是山形数组，所以我们不需要删除任何元素。

示例 2：
输入：nums = [2,1,1,5,6,2,3,1]
输出：3
解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。

提示：
3 <= nums.length <= 1000
1 <= nums[i] <= 109
题目保证 nums 删除一些元素后一定能得到山形数组。
'''


### 方法一：贪心 + 二分查找
# 这题需要借助最长递增子序列，参考0300-最长递增子序列
# 时间复杂度：O(n log n)
# 空间复杂度：O(n)
class Solution:
    def LIS(self, nums):
        lis, g = [], []
        for x in nums:
            j = bisect_left(g, x)
            lis.append(j + 1)
            if j == len(g):  # 在 g 的末尾添加元素
                g.append(x)
            else:  # 修改元素
                g[j] = x
        return lis
    
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        forward = self.LIS(nums)  # 从左到右的最长递增子序列
        backward = self.LIS(nums[::-1])[::-1]  # 从右到左的最长递增子序列
        res = 0
        for i in range(n):
            if forward[i] > 1 and backward[i] > 1:
                res = max(res, forward[i] + backward[i] - 1)
        return n - res