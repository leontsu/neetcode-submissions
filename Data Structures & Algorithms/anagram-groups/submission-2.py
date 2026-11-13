class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for w in strs:
            sortedW = tuple(sorted(w))
            if sortedW in hashmap:
                hashmap[sortedW].append(w)
            else:
                hashmap[sortedW] = [w]

        return list(hashmap.values())