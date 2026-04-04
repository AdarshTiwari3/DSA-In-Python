from typing import List


class Solution:
    def encode(self, s: List[str]):
        # code here
        # lets add length + delimiter and append it before the actual string to encode it

        encoded_list = []
        for word in s:
            encoded_list.append(str(len(word)))
            encoded_list.append("$")
            encoded_list.append(word)

        encoded_string = "".join(encoded_list)
        return encoded_string

    def decode(self, s):
        # code here

        ans, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "$":
                j += 1

            length = int(s[i:j])

            substring = s[j + 1 : j + 1 + length]

            ans.append(substring)
            i = j + 1 + length

        return ans


# TC=> O(n)
# SC=> O(n)
