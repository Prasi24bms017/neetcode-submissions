class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(index,curr_comb,curr_sum):
            if curr_sum==target:
                result.append(curr_comb.copy())
                return 
            if curr_sum>target or index==len(nums):
                return 
            curr_comb.append(nums[index])
            backtrack(index, curr_comb, curr_sum+nums[index])
            curr_comb.pop()
            backtrack(index+1,curr_comb,curr_sum)

        backtrack(0,[],0)
        return result