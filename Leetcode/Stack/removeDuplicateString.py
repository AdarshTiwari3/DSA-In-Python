class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        stack=[]
        visited=set()
        lastVisitedIndex={}
        for i in range(n):
            lastVisitedIndex[s[i]]=i
        print(lastVisitedIndex)
        for i in range(n):
            if s[i] in visited:
                continue
            else:
                while stack and stack[-1]>s[i] and i<lastVisitedIndex[stack[-1]]:
                    # remove the last visited and stack
                    visited.remove(stack.pop())
                # add the char in stack and mark as visited
                stack.append(s[i])
                visited.add(s[i])
                print("stack=",stack)
        




        return "".join(stack)

        