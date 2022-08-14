# 4g 기지국을 5g로 바꾸려고함
# 5g 기지국은 4g기지국보다 전달범위가 좁음
# 5g 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려고함
# N: 200,000,000 이하의 자연수
# stations는 오름차순으로 정렬되어 있음

def solution(n, stations, w):
    # 설치된곳을 기준으로 자름
    
    apartment_block = []
    cur_position = 1
    low_bound = 0
    upper_bound = 0
    
    # stations마다 block으로 잘라서 block에 최소로 필요한 station의 수를 구함
    for station in stations:
        
        low_bound = station - w
        upper_bound = station + w + 1
        
        if low_bound - cur_position > 0:
            apartment_block.append(low_bound - cur_position)
        
        cur_position = upper_bound
    
    if upper_bound <= n:
        apartment_block.append(n - upper_bound + 1)
    
    answer = 0
    
    for a_b in apartment_block:
        answer += a_b // (2*w + 1) + 1 if a_b % (2*w + 1) != 0 else a_b // (2*w + 1) 

    return answer
