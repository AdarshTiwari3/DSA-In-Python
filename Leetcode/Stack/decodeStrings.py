class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]==']':
                #decoding happens here
                #get the inner substring, pop the stack until we get opening brackets [                
                inner=""
                while stack[-1]!='[':
                    # append in the starting
                    inner=stack[-1]+inner
                    stack.pop()

                # now we got the substring, now remove the [ opening
                stack.pop()

                #get the k numbers

                k=""
                # this handles the case like "100[leetcode]"
                while stack and stack[-1].isdigit():
                    # put the number in the k
                    # append in the start to maintain the numbers
                    k=stack[-1]+k
                    stack.pop()

                #now append the inner string in  the stack for k times
                stack.append(int(k)*inner)
            else:
                stack.append(s[i])

        return "".join(stack)
        
sol=Solution()
print(sol.decodeString("3[a]2[bc]")) #"aaabcbc"
print(sol.decodeString("3[a2[c]]")) #"accaccacc"
print(sol.decodeString("2[abc]3[cd]ef")) #"abcabccdcdcdef"
print(sol.decodeString("100[leetcode]")) #"