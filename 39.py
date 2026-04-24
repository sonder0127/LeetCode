class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return
            if i==len(candidates) or left<candidates[i]:
                return
            #不选
            dfs(i+1, left)
            #选
            path.append(candidates[i])
            dfs(i, left-candidates[i])
            path.pop()
        dfs(0, target)
        return ans