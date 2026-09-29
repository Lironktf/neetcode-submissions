class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        arr = []

        for i in range(len(nums) + 1): 
            arr.append([])
        
        for num in nums:
            freq[num] += 1
        for key, val in freq.items():
            arr[val].append(key)

        result = []

        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                result.append(num)
                if(len(result) == k):
                    return result

        return result

               