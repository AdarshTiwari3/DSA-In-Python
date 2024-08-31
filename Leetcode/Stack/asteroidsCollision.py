class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        i=len(asteroids)-1
        stack.append(asteroids[i])
        i=i-1
        while i >=0:
            while stack and (stack[-1]<0 and asteroids[i]>0):
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    break
                else:
                    break
                
            
            else: 
                stack.append(asteroids[i])
            
            i-=1
        return stack[::-1]
    

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        
        for i in range(len(asteroids)):
            while stack and (stack[-1]>0 and asteroids[i]<0):
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    
                break
                
            
            else: 
                stack.append(asteroids[i])
            
        
        return stack
        
        