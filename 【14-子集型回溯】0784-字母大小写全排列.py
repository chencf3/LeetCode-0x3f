'''
给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。

示例 1：
输入：s = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

示例 2:
输入: s = "3z4"
输出: ["3z4","3Z4"]

提示:
1 <= s.length <= 12
s 由小写英文字母、大写英文字母和数字组成
'''


### 方法一：枚举选项
# 时间复杂度：O(n * 2 ^ n)
# 空间复杂度：O(n)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        res, path = [], [''] * n
        def dfs(i):
            if i == n:  # 终止条件
                res.append(''.join(path))
                return
            if s[i].isdigit():  # 如果是数字
                path[i] = s[i]
                dfs(i + 1)
            else:  # 如果是字母
                for c in [s[i].lower(), s[i].upper()]:
                    path[i] = c
                    dfs(i + 1)
        dfs(0)
        return res
    
# 本题必须选，因此不能用选或不选的思路