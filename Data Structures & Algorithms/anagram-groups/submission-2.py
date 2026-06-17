class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mapper = {}

        for wd in strs:
            upd = "".join(sorted(wd))
            if upd not in mapper:
                mapper[upd] = []
            mapper[upd].append(wd)

        for key, value in mapper.items():
            result.append(value)

        return result

        