def nextSmallerElement(arr,n):
    # Write your code here.
    i=n-1
    stack=[]
    ans=[]
    while i >= 0:
        while len(stack)>0 and stack[-1]>=arr[i]:
            stack.pop()
        #if stack is empty
        
        if not stack:
            ans.append(-1)
        else:
            #else append the smaller element
            ans.append(stack[-1])
        # print("stack=",stack,"arr=",arr[i])
        stack.append(arr[i])

        i-=1
        
    return ans[::-1]

check=nextSmallerElement([2,1,4,3],4)
print(check) 