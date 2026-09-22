class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if len(stack) > 0 and hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
        return True if len(stack) == 0 else False