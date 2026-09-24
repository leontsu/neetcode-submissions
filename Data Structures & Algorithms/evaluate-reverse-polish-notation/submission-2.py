class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for r in range(len(tokens)):
            if (tokens[r] == "+"):
                curSum = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(curSum)
            elif (tokens[r] == "-"):
                curDiff = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curDiff)
            elif (tokens[r] == "*"):
                curProduct = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curProduct)
            elif (tokens[r] == "/"):
                curQuotient = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curQuotient)
            else:
                stack.append(tokens[r])

        return int(stack[-1])