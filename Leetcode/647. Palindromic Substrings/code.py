class Solution:
    def countSubstrings(self, s: str) -> int:
         
        answer = 1
        
        for i in range(len(s)-1):
            center_l, center_r = i, i
            # 중심이 한개
            while center_l>-1 and center_r<len(s):
                if s[center_l] == s[center_r]:
                    answer += 1
                    center_l -= 1
                    center_r += 1
                else:
                    break
            
            
            # 현재 값과 다음값이 같다면(중심이 두개)
            center_l = i
            center_r = i + 1
            while center_l>-1 and center_r<len(s):
                if s[center_l] == s[center_r]:
                    answer += 1
                    center_l -= 1
                    center_r += 1
                else:
                    break
                    
        return answer
