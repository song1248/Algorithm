
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        
        answer = []
        
        sorted_flowers = sorted(flowers, key = lambda x : x[0])
        reverse_sorted_flowers = sorted(flowers, key = lambda x : x[1])
        
        def bisect(flowers, p, position):
            
            left = 0
            right = len(flowers)
            
            while left < right:
                mid = left + (right-left) // 2
                if flowers[mid][position] < p:
                    left = mid + 1
                else:
                    right = mid

            return right
        
        for p in persons:
            
            a = bisect(sorted_flowers, p+1, 0)
            b = bisect(reverse_sorted_flowers, p, 1)

            answer.append(a - b)
        
        return answer
