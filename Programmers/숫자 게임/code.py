import heapq
def solution(A, B):
    # B팀의 작은 수부터 A 팀에 매칭
    # n^2은 불가능
    # sort 대신 heapq로 시간복잡도를 줄임
    
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    
    for i in range(len(A)):
        
        A_poped = heapq.heappop(A)
        B_poped = heapq.heappop(B)
        
        while B and A_poped >= B_poped:
            B_poped = heapq.heappop(B)
        
        if A_poped < B_poped:    
            answer += 1
        
        if not B:
            break
        
    return answer
