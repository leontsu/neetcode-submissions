class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            # char_count = s.count(c)
            hashmap[s[c]] = hashmap.get(s[c], 0) + 1
            hashmap[t[c]] = hashmap.get(t[c], 0) - 1

        for value in hashmap.values():
            if value != 0:
                return False
        return True