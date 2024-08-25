class Solution:
    def maxDepth(self, s: str) -> int:
        depth=cnt=0
        for i in range(len(s)):
            if s[i]=='(':
                cnt+=1
            elif s[i]==')':
                cnt-=1
            # print("depth=",depth,"cnt=",cnt)
            depth=max(depth,cnt)
        return depth

sol=Solution()
print(sol.maxDepth("(1+(2*3)+((8)/4))+1")) #3