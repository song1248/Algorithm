# 로그데이터 분석 -> 초당 최대 처리량
# 초당 최대 처리량은 ㅇ응답완료 여부에 관계없이 1초간 처리하는 요청의 최대갯수
# 처리시간은 시작과 끝 시간을 포함

def solution(lines):
    
    max_time = 0
    min_time = float('inf')
    
    def preprocessing(x):
        nonlocal max_time
        nonlocal min_time
        
        # 필요한 부분만 파싱
        x = x.split(' ')[1:]
        # end_time 전처리
        tmp_time = x[0].split(':')
        tmp_time[2] = tmp_time[2].replace(".", "")
        end_time = 0
        for i, t in enumerate([60*60*1000, 60*1000, 1]):
            end_time += int(tmp_time[i]) * t
        # delay_time 전처리
        delay_time = int(x[1].replace(".", "").replace("s", "")[::-1].zfill(4)[::-1])
        
        start_time = end_time - delay_time + 1
        
        max_time = max(max_time, end_time)
        min_time = min(min_time, start_time)
        
        return start_time, end_time

    lines = list(map(preprocessing, lines))
    
    memo = [0 for i in range(max_time-min_time+1+999)]
    
    answer = 0
    for start_t, end_t in lines:
        for t in range(start_t-min_time, end_t-min_time+1+999):
            memo[t] += 1
            answer = max(memo[t], answer)
            
    return answer
