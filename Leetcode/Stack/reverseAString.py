class Solution:
    def reverseWords(self, s: str) -> str:
        stack=[]
        i=0
        while i < len(s):
            substr=""
            if s[i]==' ':
                substr=""
                i+=1
                continue
            
            while i < len(s) and s[i] != ' ':
                substr+=s[i]
                i+=1
            print("word=",substr)
            stack.append(substr)
            substr=""
        

        return " ".join(stack[::-1])

sol=Solution()
print(sol.reverseWords("the sky is blue")) #"blue is sky the"