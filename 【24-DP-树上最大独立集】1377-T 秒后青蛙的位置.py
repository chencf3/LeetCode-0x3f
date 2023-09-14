'''
给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 n。青蛙从 顶点 1 开始起跳。规则如下：
在一秒内，青蛙从它所在的当前顶点跳到另一个 未访问 过的顶点（如果它们直接相连）。
青蛙无法跳回已经访问过的顶点。
如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。
无向树的边用数组 edges 描述，其中 edges[i] = [ai, bi] 意味着存在一条直接连通 ai 和 bi 两个顶点的边。
返回青蛙在 t 秒后位于目标顶点 target 上的概率。与实际答案相差不超过 10-5 的结果将被视为正确答案。

示例 1：
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
输出：0.16666666666666666 
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有 1/2 的概率跳到顶点 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。 

示例 2：
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
输出：0.3333333333333333
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳到顶点 7 。 

提示：
1 <= n <= 100
edges.length == n - 1
edges[i].length == 2
1 <= ai, bi <= n
1 <= t <= 50
1 <= target <= n
'''


### 方法一：
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = [[] for _ in range(n + 1)]
        g[1] = [0]  # 减少额外判断的小技巧
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建树
        ans = 0

        def dfs(x: int, fa: int, left_t: int, prod: int) -> True:
            # t 秒后必须在 target（恰好到达，或者 target 是叶子停在原地）
            if x == target and (left_t == 0 or len(g[x]) == 1):
                nonlocal ans
                ans = 1 / prod
                return True
            if x == target or left_t == 0:
                return False
            for y in g[x]:  # 遍历 x 的儿子 y
                if y != fa and dfs(y, x, left_t - 1, prod * (len(g[x]) - 1)):
                    return True  # 找到 target 就不再递归了
            return False  # 未找到 target

        dfs(1, 0, t, 1)
        return ans
    

### 方法二：
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = [[] for _ in range(n + 1)]
        g[1] = [0]  # 减少额外判断的小技巧
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建树

        def dfs(x: int, fa: int, left_t: int) -> int:
            # t 秒后必须在 target（恰好到达，或者 target 是叶子停在原地）
            if left_t == 0:
                return x == target
            if x == target:
                return len(g[x]) == 1
            for y in g[x]:  # 遍历 x 的儿子 y
                if y != fa:  # y 不能是父节点
                    prod = dfs(y, x, left_t - 1)  # 寻找 target
                    if prod: return prod * (len(g[x]) - 1)  # 乘上儿子个数，并直接返回
            return 0  # 未找到 target

        prod = dfs(1, 0, t)
        return 1 / prod if prod else 0