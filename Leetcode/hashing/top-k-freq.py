from typing import List
import heapq


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


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ans = []
        for num in nums:
            if num in mp:
                mp[num] += 1

            else:
                mp[num] = 1

        # we will use max-heap to get top k freq elements but in python <3.14 we have only minheap so we will take values in negative so that it works like that
        max_heap = []

        for num, count in mp.items():
            heapq.heappush(max_heap, (-count, num))

        # get top k

        for _ in range(k):
            ans.append(heapq.heappop(max_heap)[1])

        return ans


# TC=> O(n log k) SC=> O(n)


# using bucket sort
class SolutionBucketSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ans = []
        for num in nums:
            if num in mp:
                mp[num] += 1

            else:
                mp[num] = 1

        # use bucket sort here to create the bucket of count and nums and store nums on a particular count as an index
        bucket = [
            [] for _ in range(len(nums) + 1)
        ]  # its not a 2D array it is buckets on the index like on 1st it which is count 1 will have bucket [3] and count 2 will have bucket [2] and count 3 will have bucket [1] , these are the values for which count is calculated

        # fill the values inside bucket

        for num, count in mp.items():
            bucket[count].append(
                num
            )  # it will add the number/value for a particular count as an index

        # now traverse in reverse direction to get freq top k because we have stored the count in that way only

        for ind in range(
            len(bucket) - 1, 0, -1
        ):  # as we have taken 0th index extra as count 0 is not possible here
            for num in bucket[ind]:  # get the top k elements from each bucket index
                ans.append(num)

                if len(ans) == k:
                    return ans


# TC=> O(n) # as we have buckets in that way it totally depends on bucket creation
# SC=> O(n)
