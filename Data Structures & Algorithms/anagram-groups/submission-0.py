class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result: Dict[str, List[str]] = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in result:
                result[key].append(s)
            else:
                result[key] = [ s ]

        return [x for x in result.values()]

        