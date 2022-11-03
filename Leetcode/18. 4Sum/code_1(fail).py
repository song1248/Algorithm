class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        answer_seen = set()
        answer = []        
        nums = sorted(nums)
        
        
        Q = deque([[[],0]])
        
        while Q:
            
            tmp_list, idx = Q.popleft()
            
            if idx >= len(nums) or len(tmp_list) >= 4:
                if len(tmp_list) < 4:
                    continue
                if sum(tmp_list) == target:
                    seen.add(tuple(tmp_list+['/',idx]))
                    if tuple(tmp_list) in answer_seen:
                        continue
                    answer_seen.add(tuple(tmp_list))
                    answer.append(tmp_list)  
                continue
            
            if tuple(tmp_list+['/',idx]) in seen:
                continue
            seen.add(tuple(tmp_list+['/',idx]))
            
            Q.append([tmp_list, idx+1])
            Q.append([tmp_list+[nums[idx]], idx+1])


        return answer
