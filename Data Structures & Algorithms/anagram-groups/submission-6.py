from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto = defaultdict(list)
        for string in strs:
            count = [0]* 26 # 26 letters in the alphabet
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            dicto[tuple(count)].append(string)
        return list(dicto.values())
        
        
        # dicto = defaultdict(list)
        # for string in strs:
        #     dict_string = Counter(string)
        #     dicto[frozenset(dict_string.items())].append(string)
        
        # return [x for x in dicto.values()]
        