class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if stack:
                j = len(stack) - 1
                while stack and stack[j][1] < temperatures[i]:
                    result[stack[j][0]] = i - stack[j][0]
                    stack.pop()
                    j = len(stack) - 1
            stack.append([i, temperatures[i]])

        return result