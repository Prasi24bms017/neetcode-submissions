class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        used=set()
        def backtrack(comb):
            if len(comb)==len(nums):
                result.append(comb[:])
                return
            for n in nums:
                if n in used :
                    continue
                else:
                    used.add(n)
                    comb.append(n)
                    backtrack(comb)
            
                    comb.pop()
                    used.remove(n)
        backtrack([])
        
        return result
        
        

            

        