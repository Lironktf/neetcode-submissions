class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > stack[-1][1]:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, temp])
            #38, 36, 35
        return result

        