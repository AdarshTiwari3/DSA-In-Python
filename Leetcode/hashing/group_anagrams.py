from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in mp:
                mp[key].append(word)

            else:
                mp[key] = [word]

        return list(mp.values())


# TC=> O(n x (m log m)) where n is strs size and m is a word size at any index

# SC=> O(n x m)
