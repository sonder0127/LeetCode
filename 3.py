class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = defaultdict(int)
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            charMap[ch]+=1
            while charMap[ch]>=2:
                charMap[s[left]]-=1
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len
        # cnt_map = defaultdict(int)
        # max_len = 0
        # left = 0
        # for right, c in enumerate(s):
        #     cnt_map[c]+=1
        #     while cnt_map[c]>1:
        #         cnt_map[s[left]] -= 1
        #         left+=1
        #     max_len = max(max_len, right-left+1)
        # return max_len
        
        # num_set = set()
        # max_len = 0
        # left = 0
        # for right, c in enumerate(s):
        #     while c in num_set:
        #         num_set.remove(s[left])
        #         left+=1
        #     num_set.add(c)
        #     max_len = max(max_len, right-left+1)
        # return max_len



