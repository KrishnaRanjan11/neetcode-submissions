class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for char in strs:
            key = "".join(sorted(char))
            g[key].append(char)
        return list(g.values())

