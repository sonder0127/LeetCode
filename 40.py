class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        combinations = []
        path = []
        def dfs(i, left):
            if left==0:
                combinations.append(path.copy())
                return
            #没有可选的数字了
            if i == n:
                return

            #所选元素之和无法等于target
            x = candidates[i]
            if left<x:
                return
            
            #选x
            path.append(x)
            dfs(i+1, left-x)
            path.pop()

            #不选x
            #去除重复的情况
            i+=1
            while i<n and candidates[i]==x:
                i+=1
            dfs(i, left)
            
            
        dfs(0, target)
        return combinations