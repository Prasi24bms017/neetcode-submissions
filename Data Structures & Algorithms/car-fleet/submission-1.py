class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pairs=list(zip(position,speed))
        pairs.sort(key=lambda x:x[0], reverse =True)
        for pos, spd in pairs:
            time=(target-pos)/spd
            if not stack:
                stack.append(time)
            else:
                if time>stack[-1]:
                    stack.append(time)
                else:
                    pass
        return len(stack)
        
        