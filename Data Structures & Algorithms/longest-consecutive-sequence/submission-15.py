class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        if len(numbers) == 0:
            return 0
        
        longest = 0
        cur = min(numbers)
        curLen = 1

        while(len(numbers) > 0):
            if (cur + 1) in numbers:
                curLen += 1
                numbers.remove(cur)
                cur = cur + 1
            else:
                longest = max(longest, curLen)
                curLen = 1
                numbers.remove(cur)
                if len(numbers) != 0:
                    cur = min(numbers)
                
        return longest

