def solution(money):

    def exploer(money):
        
        cur_idx = 0
        
        dp = [ 0 for i in range(len(money))]
        
        dp[cur_idx] = money[cur_idx]
        
        len_money = len(money)
        
        for _ in range(len_money-1):
            
            cur_idx += 1  
     
            if dp[cur_idx-1] < money[cur_idx] + dp[(cur_idx-2+len_money)%len_money]:
                dp[cur_idx] = money[cur_idx] + dp[(cur_idx-2+len_money)%len_money]
            else:
                dp[cur_idx] = dp[cur_idx-1]
        # print(dp)
        return dp[-2], dp[-1]
        
    # 첫 값을 사용하면 끝 값을 사용하면 안됨
    # 첫 값을 사용했을때와 사용하지 않았을때의 값이 같다면 첫값을 사용하지 않은것
    # 첫 값을 사용했다면 마지막 값을 사용하지 않은 dp[-2]를 사용
    
    started_first = exploer(money)
    started_second = exploer(money[1:])
    # 첫값을 사용 하지 않았다면 started_first[-1]
    # 첫값을 사용 했다면 
    # 첫값을 사용한 경우에서 마지막을 사용하지않은값 과 첫값을 사용하지않은 경우의 마지막 값을 사용한다.
    
    return started_first[-1] if started_first[-1] == started_second[-1] else max(started_first[-2],started_second[-1])
