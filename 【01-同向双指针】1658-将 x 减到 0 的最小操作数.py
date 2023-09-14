'''
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

示例 1：
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。

示例 2：
输入：nums = [5,6,7,8,9], x = 4
输出：-1

示例 3：
输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
 
提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
'''


### 方法一：同向双指针
# 将nums扩展一倍，寻找长度小于等于len(nums)的最短子数组，使子数组的和为x
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        res = inf
        n = len(nums)
        nums_new = nums * 2
        tot, left = sum(nums[:n-1]), 0  # 第n-1个数后面会加上，所以这里先不加
        for right in range(n - 1, 2 * n):  # 右指针必须大于等于n - 1
            tot += nums_new[right]
            while left <= right and tot > x:
                tot -= nums_new[left]
                left += 1
            if left > n:  # 左指针必须小于等于n
                break
            if tot == x and right - left + 1 <= n:  # 左右指针间隔必须小于等于n
                res = min(res, right - left + 1)
        return -1 if res == inf else res
    

### 方法二：同向双指针
# 等价于寻找最长子数组，使子数组的和等于sum(nums) - x
# 返回结果为len(nums) - 最长子数组的长度
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        res = -1
        target = sum(nums) - x
        tot, left = 0, 0
        for right, num in enumerate(nums):
            tot += num
            while left <= right and tot > target:
                tot -= nums[left]
                left += 1
            if tot == target:
                res = max(res, right - left + 1)
        return -1 if res == -1 else len(nums) - res