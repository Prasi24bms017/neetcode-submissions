class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[]for n in range(len(nums)+1)]
        for  i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for num,cnt in count.items():
            freq[cnt].append(num)
        result=[]
        for freq_index in range(len(nums),0,-1):
            for num in freq[freq_index]:
                result.append(num)
                if len(result)==k:
                    return result


