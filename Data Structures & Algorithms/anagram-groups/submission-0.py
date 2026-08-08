from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto = defaultdict(list)
        for string in strs:
            dict_string = Counter(string)
            dicto[frozenset(dict_string.items())].append(string)
        
        return [x for x in dicto.values()]
        