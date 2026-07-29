class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={
            ')':'(',
            ']':'[',
            '}':'{'

        }
        for char in s:
            if char in ('(','[',"{"):
                stack.append(char)
            elif char in mapping: # checks for keys in map i.e. the closing brackets 
                if not stack:
                    return False
                top=stack.pop()
                if top!=mapping[char]:
                    return False
        return not stack
      

        