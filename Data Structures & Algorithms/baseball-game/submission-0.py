class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(int(stack[len(stack) - 1]) + int(stack[len(stack) - 2]))
            elif op == "D":
                stack.append(int(stack[len(stack) - 1] * 2))
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        res = 0
        for num in stack:
            res += num

        return res