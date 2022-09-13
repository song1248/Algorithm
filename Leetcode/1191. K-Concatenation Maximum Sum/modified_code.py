class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        # arr의 최대 합 구하기
        def explore(arr):
            for i in range(1, len(arr)):
                # 현재값이 양수일떄
                    # 이전값 + 현재값이 현재값보다 크면 현재값을 이전값 + 현재값 로 수정
                # 현재값이 음수일때
                    # 이전값 +현재값이 양수면 계속 더하고 아니면 0
                if arr[i]>=0:
                    arr[i] = arr[i] if arr[i] > arr[i] + arr[i-1] else arr[i] + arr[i-1]
                else: 
                    arr[i] = arr[i] + arr[i-1] if 0 < arr[i] + arr[i-1] else 0 
   
            return max(arr)

        
        # k = 1 일때는 일반탐색, k 가 1보다 클때는 max_sum_num 더해줌
        if k == 1:
            return explore(arr*k) % (10**9 + 7)
        else:
            a = explore(arr*2)
            return max(a, sum(arr)*(k-2) + a) % (10**9 + 7)
