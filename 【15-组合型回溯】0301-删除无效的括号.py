'''
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
返回所有可能的结果。答案可以按 任意顺序 返回。

示例 1：
输入：s = "()())()"
输出：["(())()","()()()"]

示例 2：
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

示例 3：
输入：s = ")("
输出：[""]

提示：
1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号
'''


### 方法一：回溯，灵神答案
# 时间复杂度：O(n * 2 ^ n)
# 空间复杂度：O(n ^ 2)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        left = right = 0  # 需要删除的左括号和右括号数量
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left:
                    left -= 1
                else:
                    right += 1
                    
        @cache  # 这里不加记忆化搜索答案WA
        def dfs(i, cl, cr, dl, dr, path):
            '''
            i: 当前索引
            cl: 当前path中左括号数量
            cr: 当前path中右括号数量
            dl: 剩余需删除左括号数量
            dr: 剩余需删除右括号数量
            path: 路径
            '''
            if i == len(s):  # 终止条件
                if dl == 0 and dr == 0:
                    res.append(path)
                return
            if cr > cl or dl < 0 or dr < 0:  # 剪枝
                return
            c = s[i]
            if c == '(':  # 如果是左括号且删除不选
                dfs(i + 1, cl, cr, dl - 1, dr, path)
            elif c == ')':  # 如果是右括号且删除不选
                dfs(i + 1, cl, cr, dl, dr - 1, path)
            dfs(i + 1, cl + (c=='('), cr + (c==')'), dl, dr, path + c)  # 不管什么符号都选
        
        dfs(0, 0, 0, left, right, '')
        return res
    

### 方法二：回溯，自己的答案
# 时间复杂度：O(n * 2 ^ n)
# 空间复杂度：O(n ^ 2)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0, 0  # 需要删除的左右括号数量
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        cnt = s.count('(') - left  # 需要保留的左右括号数量
        res, n = [], len(s)
        
        @cache
        def dfs(path, i, x, y):  # 当前已走到 s[i]，此时 path 中左右括号的数量
            if i == n:
                if x == cnt and y == cnt and len(path) == n - left - right and path not in res:
                    res.append(path)
                return
            if s[i] == '(':
                dfs(path, i + 1, x, y)  # 可以不选
                if x < cnt:
                    dfs(path + '(', i + 1, x + 1, y)  # 若左括号个数不够，还可以选左括号
            elif s[i] == ')':
                dfs(path, i + 1, x, y)  # 可以不选
                if y < x:
                    dfs(path + ')', i + 1, x, y + 1)  # 若右括号个数少于左括号，还可以选右括号
            else:
                dfs(path + s[i], i + 1, x, y)  # 字母时必须选

        dfs('', 0, 0, 0)
        return res