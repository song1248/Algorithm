class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)
        seen = set()
        answer = []
        
        if sum(nums[:4]) > target or sum(nums[-4:]) < target :
            return []
        
        for i in range(len(nums)-3):
            a = nums[i]
            if sum(nums[i+1:i+4]) + a > target:
                break
            if sum(nums[-3:]) + a < target:
                continue
            if tuple([a, nums[-3], nums[-2], nums[-1]]) in seen:
                continue
            for j in range(i+1, len(nums)-2):
                b = nums[j]
                if sum(nums[i+1:i+3]) + a + b > target:
                    break
                if sum(nums[-2:]) + a + b < target:
                    continue
                if tuple([a, b, nums[-2], nums[-1]]) in seen:
                    continue
                for k in range(j+1, len(nums)-1):
                    c = nums[k]
                    if sum(nums[i+1:i+2]) + a + b + c > target:
                        break
                    if sum(nums[-1:]) + a + b + c < target:
                        continue
                    if tuple([a, b, c, nums[-1]]) in seen:
                        continue
                    for l in range(k+1, len(nums)):
                        d = nums[l]
                        if  a + b + c + d > target:
                            break
                        if  a + b + c + d < target:
                            continue
                        if tuple([a, b, c, d]) in seen:
                            continue
                        if a + b + c + d == target:
                            seen.add(tuple([a, b, c, d]))
                            answer.append([a, b, c, d])

        return answer
