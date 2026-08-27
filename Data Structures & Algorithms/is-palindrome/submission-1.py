class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftptr = 0
        rightptr = len(s) - 1

        while leftptr < rightptr:
            while self.alphanum(s[leftptr]) == False and leftptr < rightptr:
                leftptr += 1
            while self.alphanum(s[rightptr]) == False and leftptr < rightptr:
                rightptr -= 1
            if s[leftptr].lower() == s[rightptr].lower():
                leftptr += 1
                rightptr -= 1
            else:
                return False
        return True

    def alphanum(self, c: str):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))