class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = {}

        if len(s) != len(t):
            return False

        for num in s:

            if num in freq:
                freq[num] += 1

            else:
                freq[num] = 1

        for num in t:
            if num not in freq or freq[num] == 0:
                return False

            freq[num] -= 1

        return True
