from typing import List
from collections import defaultdict


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


class SolutionOptimal:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:
            # instead sorting we will use the counter alphabet array as key but in tuple as in python we can't have list as a key

            count_alphabets = [
                0
            ] * 26  # will store the values from a..z as 0,1,2,3 index

            for ch in word:
                count_alphabets[ord(ch) - ord("a")] += 1

            # now store in map--> key will be count_alphabets array
            key = tuple(count_alphabets)

            if key in mp:
                mp[key].append(word)
            else:
                mp[key] = [word]

        return list(mp.values())


# TC=> O(n x m )
# SC=> O(n x m )


class SolutionClearnerOptimal:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for word in strs:
            # instead sorting we will use the counter alphabet array as key but in tuple as in python we can't have list as a key

            count_alphabets = [
                0
            ] * 26  # will store the values from a..z as 0,1,2,3 index

            for ch in word:
                count_alphabets[ord(ch) - ord("a")] += 1

            # now store in map--> key will be count_alphabets array
            key = tuple(count_alphabets)

            mp[key].append(
                word
            )  # defaultdict will manage automatically if key not present

        return list(mp.values())
