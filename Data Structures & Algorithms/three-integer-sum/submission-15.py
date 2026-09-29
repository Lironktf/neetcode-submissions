class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: 
                break
            if i > 0 and nums[i-1] == a: #one before handled this jon
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([a, nums[r], nums[l]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

                if nums[l] + nums[r] + nums [i] > 0:
                    r -= 1
                if nums[l] + nums[r] + nums [i] < 0:
                    l += 1
        return res
