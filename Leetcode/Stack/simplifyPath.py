class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        substr=""
        for i in range(len(path)):
            if path[i]=='/':
                if i==len(path)-1:
                    continue
                elif substr:
                    if substr=="..":
                        if stack :
                            stack.pop()
                        substr=""
                    elif substr==".":
                        substr=""
                        continue
                    else:
                        stack.append(substr)
                        substr=""

            else:
                substr=substr+path[i]
        if substr and substr!="..":
            stack.append(substr)
        elif substr=='..':
            if stack: stack.pop()
        substr=""
        # print("stack=",stack)
        if stack==[] or stack==['.']:
            return "/"
        for i in range(len(stack)):
            if stack[i]=='.' :
                substr+=""
            else:
                substr+='/'+stack[i]
        
        return substr

sol=Solution()
print(sol.simplifyPath("/home/")) #/home
print(sol.simplifyPath("/../")) #/
print(sol.simplifyPath("/home//foo/")) #/home/foo
print(sol.simplifyPath("/a/./b/../../c/")) #/c
print(sol.simplifyPath("/a/../../b/../c//.//")) #/c
print(sol.simplifyPath("/a//b////c/d//././/..")) #/a/b/c
print(sol.simplifyPath("/a/../../b/../c//.//")) #/c
print(sol.simplifyPath("/a/./b/../../c/")) #/c