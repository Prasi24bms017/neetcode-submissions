class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for i in tokens:
            if i not in ('+','-','*','/'):
                stack.append(int(i))
            else:
                second=stack.pop()
                first=stack.pop()
                if  i =='+':
                    result=first + second
                if i=='-':
                    result=first-second
                if i=='*':
                    result=first*second
                if i =='/':
                    result=first/second
                final_result=int(result)
                stack.append(final_result)
        return stack[-1]
        

        