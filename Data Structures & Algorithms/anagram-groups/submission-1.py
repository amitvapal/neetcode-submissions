class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        finale = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in finale:
                finale[key] = []

            finale[key].append(s)

        for val in finale.values():
            result.append(val)

        return result
        