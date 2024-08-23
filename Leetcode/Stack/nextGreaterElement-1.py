class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans={}
        stack=[]
        i=len(nums2)-1

        while i>=0:
            while len(stack) and stack[-1]<=nums2[i]:
                stack.pop()
            if stack == []:
                ans[nums2[i]]=-1
            else:
                ans[nums2[i]]=stack[-1]

            stack.append(nums2[i])


            i-=1
        
        final_ans=[]
        for val in nums1: # val will contain the val of list nums1 one by one
            # print("append check-",ans[val])
            final_ans.append(ans[val])
        

        return final_ans