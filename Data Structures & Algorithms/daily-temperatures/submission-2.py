class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i in range(len(temperatures)):
            for j in range(i,len(temperatures)):
                if (temperatures[j]>temperatures[i]):
                    days=j-i
                    j+=1
                    result.append(days)
                    break
                    
                   
            else:
                days=0
                   
                result.append(days)
        return result


        