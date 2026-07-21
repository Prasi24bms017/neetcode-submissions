class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for n in num_set:
            if (n-1) not in num_set:
                length=1
                start=0
               
                while (n+1) in num_set :
                    start+=1
                    length+=1
                    
                    n+=1
                longest=max(longest,length)
        return longest
                    
                



