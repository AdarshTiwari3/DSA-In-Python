class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        currentSize=0
        for i in range(len(s)):
            if s[i].isdigit():
                currentSize=currentSize*int(s[i]) # means leet2 -> leetleet
            else:
                currentSize=currentSize+1
        
        # start from the top to avoid memory exceeding condition

        for i in range(len(s)-1,-1,-1):
            if s[i].isdigit(): #size will reduce , take case as leet2- size=8, after this index size will be 8//2=4
                currentSize=currentSize//int(s[i])
                #k will also update
                k=k%currentSize
                print("k=",k, currentSize)
            else:
                if k==currentSize or k ==0:
                    return s[i]
                currentSize-=1
        return ''