from typing import List


class SolutionUsingMap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ans = []
        for num in nums:
            if num in mp:
                mp[num] += 1

            else:
                mp[num] = 1

        sorted_item = sorted(
            mp.items(), key=lambda x: x[1], reverse=True
        )  # returns list tuple

        for item in sorted_item[:k]:
            ans.append(item[0])

        return ans


# TC=> O(n log n) SC=> O(n)
