# 09:00
# n회
# t분간격
# 최대 m명 탑승가능
# 크루가 대기열에 도착하는 시각을 모은 배열 (00:00 ~ 23:59)
# 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다. 

# 셔틀을 타고 사무실에 갈 수 있는 가장 늦은 시간
def solution(n, t, m, timetable):        
    answer = ''
    
    def time_transformation(time):
        tmp = time.split(':')
        return int(tmp[0])*60 + int(tmp[1]) 
    
    def inverse_time_transformation(time):
        h = int(time / 60)
        m = time % 60
        return str(h).zfill(2)+':'+str(m).zfill(2)
    
    # timetable 변환
    timetable = list(map(time_transformation, timetable))
    timetable.sort(reverse = True)
    
    # 현재시간
    cur_time = time_transformation("09:00") 
    # 마지막 버스시간
    last_time = time_transformation("09:00") + (t)*(n-1)
    # 버스에 탈 수 있는 총 인원
    maximum_crue = m*t
    
    # 마지막 버스시간보다 늦게온사람 drop
    timetable = list(filter(lambda x : x<=last_time, timetable))
    
    n_of_passengers = 0
    # 버스 반복 t번
    for bus in range(n):
        # 일찍 온 사람부터 태우기
        n_of_passengers = m
        # 버스 자리가 남아 있고
        # 탈 사람이 있고
        # 탈 사람이 시간전에 왔으면
        last_passenger = last_time
        print(list(map(inverse_time_transformation, timetable)))
        while n_of_passengers > 0 and timetable and cur_time >= timetable[-1]:         
            last_passenger = timetable.pop()
            n_of_passengers -= 1 
        cur_time += t
    cur_time -= t
     
    # 마지막으로 탄 버스의 자리가 남아있는지 확인
    # 남아있으면 버스시간 return
    if n_of_passengers > 0:
        answer = last_time
    # 남아있지 않으면
    else:
        # 마지막으로 탄 사람의 시간보다 1분 빨리 도착
        answer =  last_passenger -1
        
    return inverse_time_transformation(answer)
