from collections import defaultdict
def solution(play_time, adv_time, logs):
    
    # 시간 변환을 위한 함수정의
    def time_transform(time):
        h, m, s = time.split(":")
        whole_time = 60*60*int(h) + 60*int(m) + int(s)
        return whole_time
    
    # 시간 변환을 위한 함수정의
    def inverse_time_transform(time):
        h = int(time/(60*60))
        time = time - h*60*60
        m = int(time/60)
        time = time - m*60
        s = int(time)
        return str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2)
                
    # preprocessing
    play_time = time_transform(play_time)
    adv_time = time_transform(adv_time)
    
    # 시작지점, 끝지점 기록을 위한 dict 선언
    start_dict = defaultdict(int)
    end_dict = defaultdict(int)
    # 시작자좀, 끝지점 기록
    for log in logs:
        start_time, end_time = log.split('-')
        start_time = time_transform(start_time)
        end_time = time_transform(end_time)
        start_dict[start_time] += 1
        end_dict[end_time] += 1
    
    # 누적시간을 기록할 list만들기
    sum_time = [ 0 for _ in range(play_time) ]
    
    # 누적시간합 구하기
    max_time = 0 # 합이 가장 큰 구간의 시간
    prv_time_sum = 0 # 이전 time의 누적합
    answer = 0 # answer
    count_mul = 0 # 현재 시청자
    
    # 시청
    for t in range(play_time):
        
        # 현재시점의 시청을 시작하는 사람이 있다면
        if t in start_dict:
            count_mul += start_dict[t]
        # 현재시점의 시청을 종료하는 사람이 있다면
        if t in end_dict:
            count_mul -= end_dict[t]
            
        # 누적합 = 이전 누적합 + 지금 시청자수
        sum_time[t] = prv_time_sum + count_mul
        
        # 광고를 현재시점 이전으로 삽입한다고 했을때 광고를 삽입할 수 있는 순간부터
        # 시청시간의 합 구하기
        # 가장 큰 값을 가지면 asnwer 갱신
        if t >= adv_time-1 and sum_time[t] - sum_time[t-adv_time] > max_time:
            max_time = sum_time[t] - sum_time[t-adv_time]
            answer = t-adv_time + 1
#             print(inverse_time_transform(t))
#             print(inverse_time_transform(t-adv_time))
                   
        prv_time_sum = sum_time[t]

    return inverse_time_transform(answer)
