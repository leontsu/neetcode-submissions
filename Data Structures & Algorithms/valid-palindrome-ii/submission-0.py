class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return True if self.isPalindrome(s,l + 1,r) or self.isPalindrome(s,l,r-1) else False
        return True

    
    def isPalindrome(self, strs, left, right) -> bool:
        l, r = left, right
        s = strs

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True