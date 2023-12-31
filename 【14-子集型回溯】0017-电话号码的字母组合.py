'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

提示：
0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
'''


### 方法一：枚举选项
# 时间复杂度：O(n * 4 ^ n)
# 空间复杂度：O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        res, path = [], []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def dfs(i):
            if i == n:
                res.append(''.join(path))
                return
            for c in dic[digits[i]]:
                path.append(c)
                dfs(i + 1)
                path.pop()  # 恢复现场

        dfs(0)
        return res
    
# 本题至少选一个，不能不选，因此不能用选或不选的思路