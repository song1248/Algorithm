# 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다.
# Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
# Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 
# 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수
import heapq
def solution(n, works):
    # 퇴근까지 남은시간 n
    # 각 일에대한 작업량 works
    # 야근 피로도를 최소화한 값을 return하는 함수
    
    works = list(map(lambda x: -x , works))
    heapq.heapify(works)
    
    
    for _ in range(n):
        poped = heapq.heappop(works)
        heapq.heappush(works, poped+1 if poped+1<1 else 0)
    
    answer = 0
    for work in works:
        answer += work**2
    
    return answer
