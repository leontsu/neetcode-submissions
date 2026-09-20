class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                r -= 1
                l += 1
            else:
                if not (self.isPalindrome(s, l, r - 1) or self.isPalindrome(s, l + 1, r)):
                    return False
                else:
                    r -= 1
                    l += 1
        return True

    def isPalindrome(self, s: str, l, r) -> bool:
        while l < r:
            if (s[l].lower() != s[r].lower()):
                return False
            else:
                r -= 1
                l += 1

        return True