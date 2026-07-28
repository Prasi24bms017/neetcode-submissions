class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need_count={}
        for char in t:
            if char in need_count:
                need_count[char]+=1
            else:
                need_count[char]=1
        window_count={}
        
        have=0
        need=len(need_count)
        result=[-1,-1]
        result_length=float('inf')
        left=0
        for right  in range(len(s)):
            char=s[right]
            if char in window_count:
                window_count[char] += 1
            else:
                window_count[char] = 1
            
            
            if char in need_count and window_count[char]==need_count[char]:
                have+=1
            while have==need:
                if (right-left+1)<result_length:
                    result_length=right-left+1
                    result=[left,right]
                left_char=s[left]
                window_count[left_char]-=1
                if left_char in need_count and window_count[left_char] < need_count[left_char]:
                    have -= 1
                left += 1
        if result_length==float('inf'):
            return ''
        else:
            return s[result[0] : result[1]+1]



        

        