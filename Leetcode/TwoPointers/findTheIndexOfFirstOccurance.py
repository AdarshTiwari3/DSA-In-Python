import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans=re.split(f"({needle})",haystack)
        p1=0
        for i in range(len(ans)):
            if ans[i]==needle or ans[i]=='':
                break
            else:
                p1+=len(ans[i])
        # print("ans=",ans)
        if p1==len(haystack):
            return -1
        return p1
        
sol=Solution()
print(sol.strStr("hello","ll")) #2