class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = defaultdict(int)

        maxf = 0
        res = 0

        for r in range(len(s)):
            seen[s[r]] += 1
            maxf = max(maxf, seen[s[r]])

            while (r - l + 1) - maxf > k:
                seen[s[l]] -= 1
                l += 1
                res -= 1
            res += 1
            r += 1
        
        return res
            