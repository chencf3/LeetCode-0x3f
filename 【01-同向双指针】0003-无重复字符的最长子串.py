'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成
'''


### 方法一：暴力枚举，超时
# 时间复杂度：O(n ^ 3)
# 空间复杂度：O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(i, j):
            dic = Counter(s[i :j + 1])
            for value in dic.values():
                if value != 1:
                    return False
            return True
        
        res = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res


### 方法二：同向双指针
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, left = 0, 0
        dic = Counter()
        for right, x in enumerate(s):
            dic[x] += 1
            while dic[x] > 1:
                dic[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res