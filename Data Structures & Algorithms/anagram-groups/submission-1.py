from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) 
        # keys: tuple of char count, values: list of words

        for s in strs:
            wordcount = [0] * 26
            for c in s:
                wordcount[ord(c) - ord("a")] += 1
            hashmap[tuple(wordcount)].append(s)

        return list(hashmap.values())