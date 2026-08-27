class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftptr = 0
        rightptr = len(s) - 1

        while leftptr < rightptr:
            temp = s[leftptr]
            s[leftptr] = s[rightptr]
            s[rightptr] = temp
            leftptr += 1
            rightptr -= 1