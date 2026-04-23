from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)

        for st in strs:
            sorted_word= ''.join(sorted(st))
            anagram_map[sorted_word].append(st)
        return list(anagram_map.values())
