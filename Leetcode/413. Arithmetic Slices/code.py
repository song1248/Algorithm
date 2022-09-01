class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        answer = 0
        count = 2
        gap = 0
        
        try:
            gap = nums[1] - nums[0]
        except:
            return 0
        
        for idx in range(2 ,len(nums)):

            # 이전의 gap과 같으면 + 1
            if nums[idx] - nums[idx-1] == gap:
                count += 1

            # 순서가 끝났을때
            else:
                if count >= 3:
                    answer += sum(range(1,count-1))
                count = 2
            
            if idx == len(nums)-1:
                if count >= 3:
                    answer += sum(range(1,count-1))
                    
            gap = nums[idx] - nums[idx-1]

        return answer
