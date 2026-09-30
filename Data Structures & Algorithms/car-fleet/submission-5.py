class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = sorted(zip(position, speed))

        for pos, speed in cars:
            t = (target - pos) / speed
            stack.append(t)
        
        counter = 1
        recent = stack[-1]
        while stack:
            if recent == stack[-1]:
                stack.pop()
                continue
            elif recent < stack[-1]:
                counter += 1
                recent = stack[-1]
            stack.pop()
        return counter


#1, 1, 12, 7, 3