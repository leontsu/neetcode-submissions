class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + "#" + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        j = 0
        while j < len(s):
            i = j
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            res.append(s[i + 1 : i + 1 + length])
            j = i + 1 + length

        return res